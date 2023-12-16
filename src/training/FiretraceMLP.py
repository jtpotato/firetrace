import torch.nn as nn


class FiretraceMLP(nn.Module):
    def __init__(self, width, depth):
        super().__init__()
        self.layers = nn.ModuleList()
        self.layers.append(nn.Linear(9, width))
        self.layers.append(nn.ReLU())

        self.layers.extend([nn.Linear(width, width), nn.ReLU()] * depth)

        self.layers.append(nn.Linear(width, 1))
        self.layers.append(nn.Softplus())

    def forward(self, x):
        result = x
        for layer in self.layers:
            result = layer(result)
        return result
