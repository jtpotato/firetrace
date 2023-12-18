import torch

from training.constants import MODEL_WIDTH, MODEL_DEPTH


def save_model(model, epoch, training_history):
    training_history[2].append(epoch / 10)
    torch.save(
        {
            "model_state_dict": model.state_dict(),
            "epochs": epoch,
            "model_size": [MODEL_WIDTH, MODEL_DEPTH],
            "history": training_history,
        },
        "models/firetrace_model.pt",
    )
