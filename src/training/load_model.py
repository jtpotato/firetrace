import os

import torch

from training.FiretraceMLP import FiretraceMLP
from training.constants import MODEL_WIDTH, MODEL_DEPTH

firetrace_model = torch.compile(
    FiretraceMLP(width=MODEL_WIDTH, depth=MODEL_DEPTH), fullgraph=True, mode="max-autotune"
)


def load_model(model_path=None):
  saved_epochs = 0
  history = [[], [], []]

  if model_path == None:
    model_path = "models/firetrace_model.pt"

  # Load from previous
  if os.path.exists(model_path):
      checkpoint = torch.load(model_path)
      firetrace_model.load_state_dict(checkpoint["model_state_dict"])
      firetrace_model.train()
      history = checkpoint["history"]

      saved_epochs = checkpoint["epochs"]

  return firetrace_model, saved_epochs, history