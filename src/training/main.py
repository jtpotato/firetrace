import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader
import torch.nn as nn
import torch

from FiretraceData import FiretraceData
from FiretraceMLP import FiretraceMLP
from FiretraceImport import FiretraceImport

X_train, X_test, y_train, y_test = FiretraceImport()

train_dataset = FiretraceData(X_train, y_train)

# print(X_train, y_train.values)

train_loader = DataLoader(dataset=train_dataset, batch_size=128, shuffle=True)

firetrace_model = FiretraceMLP()
compiled_model = torch.compile(firetrace_model)

loss_function = nn.MSELoss()
optimizer = torch.optim.Adam(compiled_model.parameters(), lr=0.00001)

# Load from previous
if os.path.exists("models/firetrace_model.pt"):
  checkpoint = torch.load("models/firetrace_model.pt")
  compiled_model.load_state_dict(checkpoint['model_state_dict'])
  compiled_model.train()

  saved_epochs = checkpoint['epochs']
else:
  saved_epochs = 0

ADDTIONAL_EPOCHS = 10000

for epoch in range(saved_epochs, saved_epochs + ADDTIONAL_EPOCHS):
    epoch_loss = 0.0
    # Iterate over the DataLoader for training data
    for i, data in enumerate(train_loader, 0):
        # Get and prepare inputs
        inputs, targets = data
        inputs, targets = inputs.float(), targets.float()
        targets = targets.reshape((targets.shape[0], 1))

        # Zero the gradients
        optimizer.zero_grad()

        outputs = compiled_model(inputs)

        loss = loss_function(outputs, targets)

        # Perform backward pass
        loss.backward()
        optimizer.step()

        # Print statistics
        epoch_loss += loss.item()

    if epoch % 100 == 0:
        # Validate model
        test_output = compiled_model(torch.tensor(X_test).float())
        test_loss = loss_function(test_output, torch.tensor(y_test).float().reshape((y_test.shape[0], 1)))

        print(f"Epoch {epoch} | Loss: {epoch_loss / len(train_loader)} | Val Loss: {test_loss} | Sample Output: {test_output[50]}")

print(f"FINISHED TRAINING. TOTAL EPOCHS: {saved_epochs + ADDTIONAL_EPOCHS}")
torch.save({'model_state_dict': compiled_model.state_dict(), 'epochs': saved_epochs + ADDTIONAL_EPOCHS}, "models/firetrace_model.pt")