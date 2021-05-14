from yahoo_financial_data_module import Ticker

ticker = Ticker('INFY.NS')
ticker_data = ticker.get_historical_stock_price()

def marubozu_candlestick(price_dict,tolerance=None):
    if not tolerance:
        tolerance = 0.01 * (price_dict['High'] - price_dict['Low'])
    if price_dict['Close'] > price_dict['Open']:
        return int((abs(price_dict['Close'] - price_dict['High']) + abs(price_dict['Open'] - price_dict['Low'])) <= tolerance)
    return - int((abs(price_dict['Open'] - price_dict['High']) + abs(price_dict['Close'] - price_dict['Low']) <= tolerance))

# ticker_data['marubozu_pattern'] = ticker_data.apply(marubozu_candlestick,axis=1)

def hammer(df):
    high, low, open_, close = df['high'],df['low'],df['open'],df['close']
    
    return (((high - low) > 3 * (open_ - close)) and ((close - low) / (.001 + high - low) > 0.6) and 
                     ((open_ - low) / (.001 + high - low) > 0.6))

# ticker_data['hammer_pattern'] = ticker_data.apply(hammer,axis=1)