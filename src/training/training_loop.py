import numpy as np
import torch
import torch.nn as nn

from training.Visualise import generate_visualisation, graph_loss
from training.train_model import train_model
from training.save_on_improvement import save_model_if_improved
from training.validate import validate_model
from training.load_model import load_model

device=torch.device("cpu")

loss_function = torch.compile(nn.MSELoss(), fullgraph=True, mode="max-autotune")

MODEL_WIDTH = 35
MODEL_DEPTH = 4

def train_loop(X_test, y_test, train_loader, epoch_limit, retries):
    for i in range(retries):
        firetrace_model, saved_epochs, history = load_model(width=MODEL_WIDTH, depth=MODEL_DEPTH)

        firetrace_model.to(device)

        optimizer = torch.optim.AdamW(firetrace_model.parameters(), lr=1 * 1e-4, weight_decay=1e-3)

        best_loss = np.inf
        mega_epochs_since_best = 0

        for epoch in range(saved_epochs, saved_epochs + epoch_limit):
            epoch_loss = 0.0
            for i, data in enumerate(train_loader, 0):
                inputs, targets = data
                epoch_loss += train_model(inputs, targets, firetrace_model, optimizer, loss_function=loss_function, device=device)

            if epoch % 10 == 0:
                test_loss, test_output = validate_model(X_test, y_test, firetrace_model, loss_function=loss_function, device=device)

                print(
                    f"Epoch {epoch} | Loss: {epoch_loss / len(train_loader)} | Val Loss: {test_loss} | Sample Output: {test_output[50].item()} | Actual: {y_test[50]}"
                )

                history[0].append(epoch_loss / len(train_loader))
                history[1].append(test_loss)

                generate_visualisation(firetrace_model, epoch)

                best_loss, increment = save_model_if_improved(test_loss, best_loss, firetrace_model, epoch, MODEL_WIDTH, MODEL_DEPTH, history)
                mega_epochs_since_best += increment

                if mega_epochs_since_best > 50:
                    print("EARLY STOPPING - MAY COMMENCE ANOTHER RETRY")
                    break

                graph_loss(history)

    print("ALL RETRIES CONCLUDED.")