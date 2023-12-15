import torch


def save_model_if_improved(test_loss, best_loss, model, epoch, width, depth, training_history):
    if test_loss < best_loss:
        training_history[2].append(epoch / 10)
        best_loss = test_loss
        torch.save(
            {
                "model_state_dict": model.state_dict(),
                "epochs": epoch,
                "model_size": [width, depth],
                "history": training_history,
            },
            "models/firetrace_model.pt",
        )
        print(f"SAVED MODEL AT EPOCH {epoch}")
        return best_loss, 0
    else:
        return best_loss, 1