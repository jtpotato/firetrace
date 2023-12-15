import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader
import torch.nn as nn
import torch

from training.FiretraceData import FiretraceData
from training.FiretraceMLP import FiretraceMLP
from training.FiretraceImport import FiretraceImport
from training.TrainLoop import train_loop

X_train, X_test, y_train, y_test = FiretraceImport()

train_dataset = FiretraceData(X_train, y_train)

# print(X_train, y_train.values)

train_loader = DataLoader(dataset=train_dataset, batch_size=64, shuffle=True)

WIDTH=40
DEPTH=15

firetrace_model = torch.compile(FiretraceMLP(width=WIDTH, depth=DEPTH), fullgraph=True, mode="max-autotune")

# Load from previous
if os.path.exists("models/firetrace_model.pt"):
  checkpoint = torch.load("models/firetrace_model.pt")
  firetrace_model.load_state_dict(checkpoint['model_state_dict'])
  firetrace_model.train()

  saved_epochs = checkpoint['epochs']
else:
  saved_epochs = 0

ADDTIONAL_EPOCHS = 4500

train_loop(X_train, X_test, y_train, y_test, train_loader, firetrace_model, saved_epochs, ADDTIONAL_EPOCHS)

print(f"FINISHED TRAINING. TOTAL EPOCHS: {saved_epochs + ADDTIONAL_EPOCHS}")
torch.save({'model_state_dict': firetrace_model.state_dict(), 'epochs': saved_epochs + ADDTIONAL_EPOCHS, 'model_size': [WIDTH, DEPTH]}, "models/firetrace_model.pt")