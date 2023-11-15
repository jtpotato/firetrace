---
title: "Firetrace"
emoji: "🔥"
colorFrom: "yellow"
colorTo: "gray"
sdk: "gradio"
python_version: "3.11"
sdk_version: "3.40.1"
app_file: "app.py"
pinned: true
fullWidth: true
---
<img src="./assets/banner.svg" alt="Firetrace Logo" />

# About
Firetrace is an AI model and web interface that predicts the severity of bushfire events at a nationwide scale, by using projected weather data. It uses a deep neural network trained on data from BOM weather observatories around the country, NASA’s MODIS satellite and the Southern Oscillation Index as well as time information to represent seasonality and climate change trends.

Read the [Report](./Firetrace%20-%20Paper.pdf)

# Using the Model
## Easiest: HuggingFace Space
Navigate to https://jtpotato-firetrace.hf.space/. Most inputs are self-explanatory. Southern Oscilation Index uses numbers as reported by the Australian Bureau of Meteorology.

Of course, you don't need to interact with this model through the HuggingFace page. You have two other options:
## Advanced: Running Locally
1. Clone the repository to some directory (preferrably on a fast SSD, although the scale of the model means it should work well on most drives)
2. Install dependencies. This may differ between installations of Python.
```bash
python3 -m pip install -r requirements.txt
```
3. Run the web server. This will make http://127.0.0.1:7860 accessible via web browser.
## Very Advanced: Using Model Weights
See [firetrace/predict.py](./firetrace/predict.py) on specific implementation details.

Essentially:
```py
loaded_model = tf.saved_model.load("./model")
data = {
    "max_t_syd": [max_temp_syd],
    "max_t_bne": [max_temp_bne],
    "time_sin": [time_sin],
    "time_cos": [time_cos],
    "soi": [soi],
    "year": [year],
}
data_df = pd.DataFrame(data=data)

prediction = loaded_model.serve(data_df)
```
*These details are correct as of 25/8/2023. Any changes will be reflected in [firetrace/predict.py](./firetrace/predict.py), however the README may not recieve updates as frequently*

# Roadmap
See [Issues](https://github.com/jtpotato/firetrace/issues)

https://docs.google.com/forms/u/0/d/e/1FAIpQLScQqeT4NGpCGj5Uvjy5yLtptGuPUQFFuHSzVSZjySyGNyE8gw/formResponse