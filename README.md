# Stock Price Movement Predictor

## Project Title
Stock Price Movement Predictor

## Description
This project is a lightweight Flask web application designed to predict the short-term movement (Up or Down) of a given stock's price. It leverages the `yfinance` library to fetch real-time stock data and provides a simple web interface for users to input a stock ticker and receive a prediction.

**Key Features:**
*   **Web Interface:** A user-friendly web form to input stock tickers.
*   **Real-time Data Fetching:** Integrates with `yfinance` to retrieve historical stock data.
*   **Placeholder Prediction:** Currently uses a random mechanism for prediction, serving as a placeholder for future integration with a trained Artificial Neural Network (ANN) model.
*   **Error Handling:** Basic error handling for invalid tickers or data fetching issues.
*   **Extensible:** Designed with clear points for integrating a Keras/TensorFlow ANN model for actual predictions.

## Installation

To set up and run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <repository_url> # Replace with your actual repository URL
    cd stock-price-movement-predictor # Or whatever your project directory is named
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    *   **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    *   **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies:**
    ```bash
    pip install Flask yfinance numpy pandas
    ```
    *Note: If you plan to integrate the ANN model, you will also need to install `tensorflow` or `keras`.*
    ```bash
    # pip install tensorflow # Uncomment and run when integrating the ANN model
    ```

## Usage

To run the application:

1.  **Ensure your virtual environment is activated.**
2.  **Start the Flask development server:**
    ```bash
    python app.py
    ```
    You should see output similar to:
    ```
     * Serving Flask app 'app'
     * Debug mode: on
     WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
    * Restarting with stat
     * Debugger is active!
     * Debugger PIN: ...
    ```

3.  **Open your web browser** and navigate to `http://127.0.0.1:5000`.

4.  **Enter a stock ticker** (e.g., `AAPL`, `GOOG`, `RELIANCE.NS`) into the input field and click the "Predict" button. The application will display a predicted movement (Up/Down) and the last closing price.

## Project Structure

```
.
├── app.py
├── templates/
│   └── index.html
└── README.md
```

*   **`app.py`**: The main Flask application file. It handles routing, fetches stock data using `yfinance`, and renders the HTML templates. It also contains the placeholder logic for stock movement prediction and is designed to load a Keras ANN model.
*   **`templates/`**: This directory stores all HTML template files used by Flask.
    *   **`index.html`**: The main user interface template, containing the stock ticker input form and displaying prediction results.

## Technologies Used

*   **Python**: The core programming language.
*   **Flask**: A micro web framework for building the web application.
*   **yfinance**: A library used to download historical market data from Yahoo! Finance.
*   **NumPy**: Essential for numerical operations, particularly for array manipulation.
*   **Pandas**: Used for data manipulation and analysis, especially with DataFrames for stock data.
*   **HTML/CSS**: For structuring and styling the web interface.
*   **Keras/TensorFlow (Planned)**: The project is structured to integrate a trained Artificial Neural Network model for actual predictions, which would typically be built with Keras on top of TensorFlow.

## Scripts

The primary script to run the application is `app.py`.

*   **`python app.py`**: Starts the Flask development server.

## Configuration

*   **Debug Mode**: The Flask application runs in debug mode (`app.run(debug=True)`), which provides helpful error messages and automatically reloads the server on code changes. This should be disabled for production environments.
*   **ANN Model Path**: The application is designed to load a trained Keras model from `ann_stock_model.h5`. This file is not included in the current project structure and needs to be provided when integrating the actual prediction model.

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes and commit them (`git commit -m 'Add some feature'`).
4.  Push to the branch (`git push origin feature/your-feature-name`).
5.  Open a Pull Request.

## License

No specific license file was provided with the project. Please assume standard copyright or inquire with the project maintainer for licensing details.