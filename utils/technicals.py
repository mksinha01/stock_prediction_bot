import ta

def add_technical_indicators(df):
    df['rsi'] = ta.momentum.RSIIndicator(df['Close']).rsi()
    df['macd'] = ta.trend.MACD(df['Close']).macd()
    df['sma'] = ta.trend.SMAIndicator(df['Close'], window=14).sma_indicator()
    df.dropna(inplace=True)
    return df
