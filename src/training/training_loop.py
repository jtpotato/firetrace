import numpy as np
import torch
import torch.nn as nn

from training.train_model import train_model
from training.save_on_improvement import save_model
from training.validate import validate_model
from training.load_model import load_model
from training.firetrace_loss import FiretraceLoss
from terminal import colours
from training.visualise import draw_visualisation, graph_loss

device = torch.device("cpu")

loss_function = torch.compile(nn.MSELoss(), fullgraph=True, mode="max-autotune")


def train_loop(X_test, y_test, train_loader, epoch_limit):
    print(f"{colours.YELLOW}ENTERING TRAINING LOOP.\nMAXIMUM LENGTH OF {epoch_limit} EPOCHS.{colours.END}")

    firetrace_model, saved_epochs, history = load_model()

    firetrace_model.to(device)

    optimizer = torch.optim.AdamW(firetrace_model.parameters(), lr=4 * 1e-6, weight_decay=1e-5)

    best_loss = np.inf
    mega_epochs_since_best = 0

    for epoch in range(saved_epochs, saved_epochs + epoch_limit):
        epoch_loss = 0.0
        for i, data in enumerate(train_loader, 0):
            inputs, targets = data
            epoch_loss += train_model(
                inputs,
                targets,
                firetrace_model,
                optimizer,
                loss_function=loss_function,
                device=device,
            )

        if epoch % 10 == 0:
            test_loss, test_output = validate_model(
                X_test,
                y_test,
                firetrace_model,
                loss_function=loss_function,
                device=device,
            )

            history[0].append(epoch_loss / len(train_loader))
            history[1].append(test_loss)

            if test_loss + 1e-5 < best_loss:
                save_model(
                    firetrace_model,
                    epoch,
                    history
                )
                mega_epochs_since_best = 0
                best_loss = test_loss
                print(colours.GREEN, end="")
            else:
                mega_epochs_since_best += 1

            print(
                f"Epoch {epoch} | Loss: {epoch_loss / len(train_loader)} | Val Loss: {test_loss} | Sample Output: {test_output[50].item()} | Actual: {y_test[50]}{colours.END}"
            )

            if mega_epochs_since_best > 50:
                print(f"{colours.RED}EARLY STOPPING.{colours.END}")
                break

        if epoch % 50 == 0:
            draw_visualisation(firetrace_model, epoch)
            graph_loss(history)