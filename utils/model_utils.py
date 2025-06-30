from sklearn.preprocessing import MinMaxScaler
import numpy as np
import tensorflow as tf

def prepare_lstm_data(df, feature='Close', look_back=60):
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(df[[feature]])

    X, y = [], []
    for i in range(look_back, len(scaled_data)):
        X.append(scaled_data[i-look_back:i])
        y.append(scaled_data[i])
    return np.array(X), np.array(y), scaler

def build_lstm_model(input_shape):
    model = tf.keras.Sequential([
        tf.keras.layers.LSTM(50, return_sequences=True, input_shape=input_shape),
        tf.keras.layers.LSTM(50),
        tf.keras.layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    return model
