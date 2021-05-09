from yahoo_financial_data_module import Ticker
import pandas as pd

class indicator:
    def __init__(self):
        pass
    def RsiIndicator(self, close_price_series, period = 14):
        temp = close_price_series.diff(1)
        up = temp.where(temp > 0,0)
        down = -temp.where(temp < 0,0)
        up = up.ewm(alpha=1/period,min_periods=period,adjust=False).mean()
        down = down.ewm(alpha=1/period,min_periods=period,adjust=False).mean()
        RS = up/down
        RSI = 100 - (100/(1 + RS))
        return RSI

ticker = Ticker('INFY.NS')
ticker_data = ticker.get_historical_stock_price()
ind = indicator()
rsi_data = ind.RsiIndicator(ticker_data['Close'])
print(rsi_data.iloc[0])