from yahoo_financial_data_module import Ticker
from ta import import add_all_ta_features

ticker = Ticker('INFY.NS')
ticker_ta_data = add_all_ta_features(ticker,open='Open',close='Close',high='High',low='Low',volume='Volume')
print(ticker_ta_data.columns)