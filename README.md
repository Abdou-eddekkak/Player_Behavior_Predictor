# Player Behavior AI Dashboard

An end-to-end AI-powered web application that analyzes gameplay behavior using an LSTM neural network built with PyTorch.

The system predicts player behavior profiles such as:

- Casual
- Aggressive
- Explorer

using gameplay sequence data collected over time.

---

##  Live Demo

+ Frontend:  
player-behavior-predictor.netlify.app

 API Docs:  
https://player-behavior-predictor.onrender.com/docs

---

## Features

+ LSTM-based sequence prediction  
+ Real-time AI inference  
+ Dynamic confidence visualization with Chart.js  
+ Interactive SaaS-style frontend  
+ FastAPI backend  
+ Full-stack deployment  
+ Random gameplay sequence generation for testing  

---

## Tech Stack

### Machine Learning
- Python
- PyTorch
- LSTM Neural Networks

### Backend
- FastAPI
- Uvicorn

### Frontend
- HTML
- CSS
- JavaScript
- Chart.js

### Deployment
- Render
- Netlify

---

## Project Structure

project/
│
├── api.py
├── model.py
├── dataset.py
├── train.py
├── players.csv
├── model.pth
├── metrics.json
├── requirements.txt
└── index.html
---

## Installation:

  1. Clone Repository
    git clone YOUR_GITHUB_REPO
    cd YOUR_PROJECT
  2. Install Dependencies
    pip install -r requirements.txt
  3. Train Model
    python train.py
  5. Start API
    uvicorn api:app --reload
  6. Open Frontend
    Open index.html in your browser.
