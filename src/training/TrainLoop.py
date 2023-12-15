import torch
import torch.nn as nn

device=torch.device("cpu")

if torch.backends.mps.is_available() and torch.backends.mps.is_built():
    print("Using MPS.")
    device = torch.device("mps")

def train_loop(X_train, X_test, y_train, y_test, train_loader, compiled_model, saved_epochs, additional_epochs):
    compiled_model.to(device)

    loss_function = torch.compile(nn.MSELoss(), backend="aot_eager")

    optimizer = torch.optim.Adam(compiled_model.parameters(), lr=0.00001)

    for epoch in range(saved_epochs, saved_epochs + additional_epochs):
        epoch_loss = 0.0
        # Iterate over the DataLoader for training data
        for i, data in enumerate(train_loader, 0):
            # Get and prepare inputs
            inputs, targets = data
            inputs, targets = inputs.float().to(device), targets.float().to(device)
            targets = targets.reshape((targets.shape[0], 1))

            # Zero the gradients
            optimizer.zero_grad()

            outputs = compiled_model(inputs)

            loss = loss_function(outputs, targets)

            # Perform backward pass
            loss.backward()
            optimizer.step()

            epoch_loss += loss.item()

        if epoch % 100 == 0:
            # Validate model
            test_output = compiled_model(torch.tensor(X_test).float().to(device))
            test_loss = loss_function(test_output, torch.tensor(y_test, dtype=torch.float32, device=device).float()).item()

            print(
                f"Epoch {epoch} | Loss: {epoch_loss / len(train_loader)} | Val Loss: {test_loss} | Sample Output: {test_output[50].float()}"
            )
