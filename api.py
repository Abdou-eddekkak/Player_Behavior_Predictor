from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import torch
from model import LSTMModel

app = FastAPI()

model = LSTMModel()
model.load_state_dict(torch.load("model.pth", map_location=torch.device("cpu")))
model.eval()

labels = ["casual", "aggressive", "explorer"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
def predict(data:dict):
    seq = data["sequence"]

    x = torch.tensor([seq], dtype=torch.float32)

    output = model(x)

    probs = torch.softmax(output, dim=1).detach().numpy()[0]
    pred = int(torch.argmax(output, dim=1).item())

    return {
        "prediction": labels[pred],
        "probabilities": {
            "casual": float(probs[0]),
            "aggressive": float(probs[1]),
            "explorer": float(probs[2])
        }
    }

@app.get("/")
def root():
    return {"status": "API running"}