# config.py

# Stock symbol to predict (e.g., AAPL, MSFT, TSLA)
STOCK_SYMBOL = 'AAPL'

# Timeframe of historical data (can be '1mo', '3mo', '6mo', '1y', etc.)
DATA_PERIOD = '6mo'

# Interval between each data point (e.g., '1d' for daily, '1h' for hourly)
DATA_INTERVAL = '1d'

# LSTM Look-back window (number of previous days used for prediction)
LOOK_BACK = 60

# Number of training epochs
EPOCHS = 10

# Batch size for training
BATCH_SIZE = 32

# Minimum confidence to trigger an automatic bet
CONFIDENCE_THRESHOLD = 0.80

# Enable logging predictions
LOG_PREDICTIONS = True
