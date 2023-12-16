import torch.nn as nn
import torch

class FiretraceLoss(nn.Module):
  def __init__(self):
    super(FiretraceLoss, self).__init__()

  def forward(self, predictions, targets):
    return torch.mean(
      torch.mul(torch.pow(predictions - targets, 2), (torch.abs(targets) * 1.5 + 0.1) ** 2)
    )