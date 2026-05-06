import torch
from torch.utils.data import Dataset
import pandas as pd

class PlayerSequenceDataset(Dataset):
    def __init__(self, file):
        data = pd.read_csv(file)

        data = data.dropna()

        data = data[data.iloc[:, -1].isin([0, 1, 2])]

        print("Dataset size:", len(data))
        print("Labels:", data.iloc[:, -1].unique())

        X = data.iloc[:, :-1].values
        y = data.iloc[:, -1].values

        self.X = torch.tensor(X, dtype=torch.float32).view(-1, 5, 5)
        self.y = torch.tensor(y, dtype=torch.long)

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]