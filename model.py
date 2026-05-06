import torch.nn as nn

class LSTMModel(nn.Module):
    def __init__(self):
        super().__init__()

        self.lstm = nn.LSTM(
            input_size=5,
            hidden_size=64,
            batch_first=True
        )

        self.fc = nn.Linear(64, 3)

    def forward(self, x):
        _, (hidden, _) = self.lstm(x)
        out = hidden[-1]
        return self.fc(out)