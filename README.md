# MavericksA0127IntelOneApiHackathon

# UPCOMING CANDLE STICK PREDICTOR FOR STOCKS

In intraday trading, traders heavily rely on technical analysis for making trade decisions. Candlestick graphs are an elegant way which help traders quickly understand the past movement of
a stock’s price. They also help in understanding the market sentiment

![Screenshot 2024-10-05 081903](https://github.com/user-attachments/assets/9a13e7fa-35c7-48da-b0d2-c7a086715584)

Predicting the next candle stick in advance can help one manage risk and make wise decisions.

# About the project:

Stock prediction may seem like simple task at first glace but to its challenging to do it in real time quickly and accurately which we have implemented with an accuracy of 87-94%. 
In the project, we have focused on S&P500, but the model works for NSE and other markets too.

The users have to add their desired stock and select the candle stick pattern which they would like to check. The ML model predicts the stock price for the next 5 minutes with a 1 min interval and forms a predictive candle stick using those values. It let's the user know if the pattern is likely to be formed in the next 5 minutes.'
The user can request for a comprehensive report of the stock.

![Screenshot 2024-10-05 081925](https://github.com/user-attachments/assets/4a178b2b-64cb-452c-8b27-1589255624fa)

# Implementation:

We have used Intel's Scikit-Learn wrapper scikit-learn-intelex for importing yfinance which is used for getting real time stock data.

#![Screenshot 2024-10-05 082044](https://github.com/user-attachments/assets/67a4f9e7-90ee-4317-8067-1f6fa3cdd159)

We have used # TensorFlow to import # ARIMA for stock prediction.

![Screenshot 2024-10-05 095833](https://github.com/user-attachments/assets/6ab691a1-6a94-4f46-ab23-13d2d2577c51)

import #cLlama # 3.1-70B versatile using langchain for generation of report

![Screenshot 2024-10-05 100032](https://github.com/user-attachments/assets/1a342bf9-04a0-454e-a13b-366c1a7c9765)

# Live Demo:

![Screenshot 2024-10-05 102333](https://github.com/user-attachments/assets/bb9b00c4-ea8f-437e-bfe4-3028ff706f39)

![Screenshot 2024-10-05 102501](https://github.com/user-attachments/assets/d23e96a3-a677-45b6-a21a-1f4e7a8288cd)


# Future Plans:

1) Let the model keep tracking the stock and notify the user when their request pattern is predicted to appear.
2) Let the users track multiple stocks at once.
3) Features related to lower support and resistance lines.
4) Add more candle stick pattens and also Introduce Multiple candle stick patterns.

# Challenges Faced
Major News (good, bad) can impact the market heavily, making it difficult to predict values in such situations.

# References:
https://indjst.org/articles/predicting-a-small-cap-company-stock-price-using-python-with-best-accuracy-rate-how-the-data-science-working-for-predictions-and-accuracy-rate


