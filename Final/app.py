from flask import Flask, render_template, request
import yfinance as yf
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import json

app = Flask(__name__)

# Simulated ChatGroq-like LLM (replace with actual LLM API)
class ChatGroq:
    def invoke(self, prompt):
        # Simulate a response from the AI model (replace with real API call)
        return type('Response', (object,), {"content": f"Generated report for prompt: {prompt}"})

llm = ChatGroq()  # Initialize the LLM

# Fetch stock data function
def fetch_stock_data(ticker, period="1d", interval="1m"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period, interval=interval, prepost=False)
    return hist

# ARIMA prediction function
def arima_predict(ticker):
    stock_data = fetch_stock_data(ticker, period="1d", interval="1m")
    if len(stock_data) < 20:
        return "Not enough data for prediction."
    
    model = ARIMA(stock_data['Close'], order=(5, 1, 0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=5)
    actual_prices = stock_data['Close'].values[-5:]
    rmse = np.sqrt(mean_squared_error(actual_prices, forecast))
    
    result = {
        'forecast': forecast.tolist(),
        'actual_prices': actual_prices.tolist(),
        'rmse': rmse
    }
    
    return result

# Function to generate AI-based stock report using ChatGroq
def generate_stock_report(ticker, stock_data, patterns):
    try:
        # Convert index (datetime) to string format for JSON serialization
        stock_data_json = stock_data.copy()
        stock_data_json.index = stock_data_json.index.strftime("%Y-%m-%d %H:%M:%S")

        prompt = (
            "Generate a concise report on the stock performance, focusing on recent trends, "
            "notable candlestick patterns detected, and key insights. The data includes open, high, low, close, and volume values.\n\n"
            f"Stock Ticker: {ticker}\n"
            f"Detected Patterns: {json.dumps(patterns)}\n"
            f"Stock Data:\n{json.dumps(stock_data_json.to_dict())}\n\n"
            "Provide insights that are easy to understand for a non-expert user.\n"
            "Report:\n"
        )
        
        # Call the LLM model to generate the report
        llm_response = llm.invoke(prompt)
        return llm_response.content
    except Exception as e:
        return f"An error occurred: {e}"

# Detect candlestick patterns (stub function)
def detect_candlestick_patterns(stock_data):
    # This function should detect candlestick patterns from the stock data
    # Currently returning a static example pattern
    return {"Engulfing (Bearish)": "Detected"}

# Flask route for the homepage
@app.route('/')
def index():
    return render_template('userindex.html')

# Flask route for predicting stock prices and generating a stock report
@app.route('/predict', methods=['POST'])
def predict():
    ticker = request.form.get('stockSelect')  # Get the selected stock ticker
    pattern = request.form.get('patternSelect')  # Get the selected candlestick pattern

    # Get prediction results using ARIMA
    prediction_result = arima_predict(ticker)

    # Fetch stock data and detect patterns
    stock_data = fetch_stock_data(ticker, period="1d", interval="1m")
    detected_patterns = detect_candlestick_patterns(stock_data)

    # Check if a major pattern is detected
    if any(p in detected_patterns for p in ["Engulfing (Bearish)", "Engulfing (Bullish)", "Hammer", "Doji"]):
        major_pattern = detected_patterns
        alert_message = f"Alert: Major candlestick pattern detected for {ticker}: {major_pattern}"
        print(alert_message)

        # Ask the user if they want a report (this would normally be a UI prompt, here it's simulated)
        generate_report = request.form.get('generateReport', 'no')  # 'yes' or 'no' based on user input
        stock_report = None

        if generate_report.lower() == 'yes':
            # Generate AI-based stock report
            stock_report = generate_stock_report(ticker, stock_data, detected_patterns)

        # Render the page with the prediction, detected pattern, and optionally the report
        return render_template('userindex.html', prediction=prediction_result, pattern=major_pattern, report=stock_report)
    else:
        # No major pattern detected, just render the prediction
        return render_template('userindex.html', prediction=prediction_result, pattern="No major pattern detected")

if __name__ == '__main__':
    app.run(debug=True)
