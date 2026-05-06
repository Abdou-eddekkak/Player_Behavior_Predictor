import torch
from model import PlayerModel

model = PlayerModel()
model.load_state_dict(torch.load("model.pth"))
model.eval()

# Example player
sample = torch.tensor([[60, 8.5, 10, 2, 5]], dtype=torch.float32)

output = model(sample)
pred = torch.argmax(output, dim=1)

labels = ["casual", "aggressive", "explorer"]
print("Prediction:", labels[pred.item()])