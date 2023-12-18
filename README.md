---
title: "Firetrace"
emoji: "🔥"
colorFrom: "yellow"
colorTo: "gray"
sdk: "gradio"
python_version: "3.11"
sdk_version: "4.10.0"
app_file: "src/frontend_main.py"
pinned: true
fullWidth: true
---
<img src="./assets/banner.svg" alt="Firetrace Logo" />

# About
Firetrace is an AI model and web interface that predicts the severity of bushfire events at a nationwide scale, by using projected weather data. It uses a deep neural network trained on data from BOM weather observatories around the country, NASA’s MODIS satellite and the Southern Oscillation Index as well as time information to represent seasonality and climate change trends.

Read the [Report](./Firetrace%20-%20Paper.pdf)

# Using the Model
## Easiest: HuggingFace Space
Navigate to https://huggingface.co/spaces/jtpotato/firetrace. Most inputs are self-explanatory. Southern Oscillation Index uses numbers as reported by the Australian Bureau of Meteorology.

## Advanced: Running Locally
1. Clone the repository to some directory (preferably on a fast SSD, although the scale of the model means it should work well on most drives)
2. Ensure you are using `Python 3.11.x`. Modify the following commands to point to Python 3.11.x if need be.
3. Install dependencies. This may differ between installations of Python.
```bash
python3 -m pip install -r requirements.txt
```
3. Run the web server with `python3 src/frontend-main.py` This will make http://127.0.0.1:7860 accessible via a web browser.

## Very Advanced: Using Model Weights
Install `PyTorch` and `joblib`

```python
import torch
import joblib

checkpoint = torch.load("models/firetrace_model.pt") # Directories may be different depending on specific environment.
model = FiretraceMLP(width=checkpoint['model_size'][0], depth=checkpoint['model_size'][1])

# OPTIONAL:
# compiled_model = torch.compile(model, fullgraph=True, mode="max-autotune")
# and use compiled_model instead of model. Note that this is not compatible with some environments.

model.load_state_dict(checkpoint['model_state_dict'])
model.eval() # Prepare model for inference

# Get your input data. You may choose to do this via a numpy array. Here's how we do it.
# It's quite important that the data is presented in the same order we have here.
inputs = [soi, max_t_bne, max_t_mel, max_t_cns, max_t_pth, max_t_syd, sin_month, cos_month, year]

# Prepare scalers
x_scaler = joblib.load("models/x_scaler.save")
y_scaler = joblib.load("models/y_scaler.save")

# Scale inputs (while converting to numpy array)
scaled_inputs = x_scaler.transform(np.array(inputs).reshape(1, -1))

model_output = model(torch.tensor(scaled_inputs).float())

# Interpret the following tensor as you wish.
scaled_output = y_scaler.inverse_transform(model_output.detach().numpy().reshape(1, -1))
```

# Roadmap
See [Issues](https://github.com/jtpotato/firetrace/issues)

# Developers
Some important notes:
- `PyTorch` requires Python `< 3.12` for now.
