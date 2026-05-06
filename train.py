import torch
import json
from torch.utils.data import DataLoader
from dataset import PlayerSequenceDataset
from model import LSTMModel

dataset = PlayerSequenceDataset("players_seq.csv")
loader = DataLoader(dataset, batch_size=32, shuffle=True)

model = LSTMModel()
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

model.train()

losses = []
accuracies = []

for epoch in range(20):
    total_loss = 0
    correct = 0
    total = 0

    for x, y in loader:
        optimizer.zero_grad()

        outputs = model(x)
        loss = criterion(outputs, y)

        loss.backward()
        optimizer.step()

        total_loss += loss.item()

        _, predicted = torch.max(outputs, 1)
        total += y.size(0)
        correct += (predicted == y).sum().item()

    epoch_loss = total_loss
    epoch_acc = correct / total

    losses.append(epoch_loss)
    accuracies.append(epoch_acc)

    print(f"Epoch {epoch+1}, Loss: {epoch_loss:.4f}, Accuracy: {epoch_acc:.4f}")

torch.save(model.state_dict(), "model.pth")

with open("metrics.json", "w") as f:
    json.dump({"losses": losses, "accuracies": accuracies}, f)