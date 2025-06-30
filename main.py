from utils.data_fetcher import fetch_stock_data
from utils.technicals import add_technical_indicators
from utils.model_utils import prepare_lstm_data, build_lstm_model
import numpy as np
import config
...
def run_prediction(symbol=config.STOCK_SYMBOL):
    data = fetch_stock_data(symbol, period=config.DATA_PERIOD, interval=config.DATA_INTERVAL)
    ...
    X, y, scaler = prepare_lstm_data(data, look_back=config.LOOK_BACK)
    model = build_lstm_model((X.shape[1], X.shape[2]))
    model.fit(X, y, epochs=config.EPOCHS, batch_size=config.BATCH_SIZE, verbose=0)
    ...

def run_prediction(symbol='AAPL'):
    data = fetch_stock_data(symbol)
    data = add_technical_indicators(data)
    
    X, y, scaler = prepare_lstm_data(data)
    model = build_lstm_model((X.shape[1], X.shape[2]))
    model.fit(X, y, epochs=10, batch_size=32, verbose=0)
    
    last_sequence = X[-1].reshape(1, X.shape[1], X.shape[2])
    prediction = model.predict(last_sequence)
    predicted_price = scaler.inverse_transform(prediction)[0][0]
    
    print(f"Predicted next close price for {symbol}: ${predicted_price:.2f}")
    return predicted_price

if __name__ == "__main__":
    run_prediction()
