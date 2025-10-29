import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model

# Load your trained model
model = load_model('ann_stock_model.h5')

def predict_stock_movement(ticker):
    # For simplicity, fetch stock data (you can also use uploaded CSV)
    # Example: Using yfinance (install with pip install yfinance)
    import yfinance as yf
    data = yf.download(ticker, period="1mo", interval="1d")

    # Preprocess data (normalize, create features, etc.)
    X_test = data[['Open', 'High', 'Low', 'Close', 'Volume']].values[-1:]  # last day
    X_test = X_test / X_test.max()  # simple normalization

    # Make prediction
    pred = model.predict(X_test)
    movement = "Up" if pred[0][0] > 0.5 else "Down"
    return movement
