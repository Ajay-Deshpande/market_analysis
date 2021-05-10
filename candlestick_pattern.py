from yahoo_financial_data_module import Ticker

ticker = Ticker('INFY.NS')
ticker_data = ticker.get_historical_stock_price()

def marubozu_candlestick(price_dict,tolerance=None):
    if not tolerance:
        tolerance = 0.005 * price_dict['Close']
    if price_dict['Close'] > price_dict['Open']:
        return int((abs(price_dict['Close'] - price_dict['High']) + abs(price_dict['Open'] - price_dict['Low'])) <= tolerance)
    return - int((abs(price_dict['Open'] - price_dict['High']) + abs(price_dict['Close'] - price_dict['Low']) <= tolerance))

ticker_data['marubozu_?'] = ticker_data.apply(marubozu_candlestick,axis=1)