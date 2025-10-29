from flask import Flask, render_template, request
import yfinance as yf
import numpy as np
import pandas as pd
# from tensorflow.keras.models import load_model  # Uncomment when you have a trained model

app = Flask(__name__)  # Flask app instance

# ------------------------------
# Uncomment and load your trained ANN model when ready
# model = load_model('ann_stock_model.h5')
# ------------------------------

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        ticker = request.form['ticker'].upper().strip()  # Clean user input

        try:
            # Fetch the last 30 days of stock data
            data = yf.download(ticker, period="1mo", interval="1d")
            
            if data.empty:
                return render_template('index.html', prediction_text=f"No data found for '{ticker}'")

            # ✅ Fix: ensure last_close is a float, not a Series
            last_close = float(data['Close'].iloc[-1])

            # Stub prediction — replace this with your ANN model logic later
            movement = "Up" if np.random.rand() > 0.5 else "Down"

            # Example ANN replacement (when your model is ready)
            # X_test = preprocess_data(data)
            # prediction = model.predict(X_test)
            # movement = "Up" if prediction[0][0] > 0.5 else "Down"

            return render_template(
                'index.html',
                prediction_text=f"Predicted movement for {ticker}: {movement} (Last Close: {last_close:.2f})"
            )

        except Exception as e:
            return render_template('index.html', prediction_text=f"Error: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True)
