def train_model(inputs, targets, model, optimizer, loss_function, device):
    inputs, targets = inputs.float().to(device), targets.float().to(device)
    targets = targets.reshape((targets.shape[0], 1))

    optimizer.zero_grad()

    outputs = model(inputs)

    loss = loss_function(outputs, targets)

    loss.backward()
    optimizer.step()

    return loss.item()