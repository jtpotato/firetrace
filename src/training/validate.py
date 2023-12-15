import torch
import torch.nn as nn

def validate_model(X_test, y_test, model, loss_function, device):
    test_output = model(torch.tensor(X_test).float().to(device))
    test_loss = loss_function(test_output, torch.tensor(y_test, dtype=torch.float32, device=device).float()).item()

    return test_loss, test_output