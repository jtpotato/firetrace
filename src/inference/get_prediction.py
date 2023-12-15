import joblib
import numpy as np
import torch
from training.FiretraceMLP import FiretraceMLP

checkpoint = torch.load("models/firetrace_model.pt")

model = FiretraceMLP(width=checkpoint['model_size'][0], depth=checkpoint['model_size'][1])
compiled_model = torch.compile(model)

compiled_model.load_state_dict(checkpoint['model_state_dict'])
compiled_model.eval()

x_scaler = joblib.load("models/x_scaler.save")
y_scaler = joblib.load("models/y_scaler.save")

def get_prediction(soi, max_t_bne, max_t_mel, max_t_cns, max_t_pth, max_t_syd, sin_month, cos_month, year):
    inputs = [soi, max_t_bne, max_t_mel, max_t_cns, max_t_pth, max_t_syd, sin_month, cos_month, year]
    scaled_inputs = x_scaler.transform(np.array(inputs).reshape(1, -1))

    model_output = compiled_model(torch.tensor(scaled_inputs).float())

    scaled_output = y_scaler.inverse_transform(model_output.detach().numpy().reshape(1, -1))
    return scaled_output