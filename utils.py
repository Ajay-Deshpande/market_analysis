import numpy as np
import pandas as pd
from yahoo_financial_data_module import Ticker

ticker = Ticker('INFY.NS')
ticker_data = ticker.get_historical_stock_price()

def ADXIndicator(high,low,close,smoothen_window = 14):
    
    high_low_range, positivity, negativity = (high - low), (high - high.shift(1)), (low - low.shift(1))
    true_range = pd.DataFrame([high_low_range,positivity,negativity]).max(axis=1)

    DM_pos, DM_neg = np.where(positivity > negativity, positivity,0), np.where(positivity < negativity, negativity,0)

    smoothened_DM_pos = DM_pos.rolling(smoothen_window).sum() - DM_pos.rolling(smoothen_window).mean() + DM_pos
    smoothened_DM_neg = DM_neg.rolling(smoothen_window).sum() - DM_neg.rolling(smoothen_window).mean() + DM_neg

    smoothened_true_range = true_range.rolling(smoothen_window).sum() - true_range.rolling(smoothen_window).mean() + true_range

    DX = ((smoothened_DM_pos - smoothened_DM_neg) * 100) / (smoothened_DM_pos + smoothened_DM_neg)

    DI_neg = (smoothened_DM_neg * 100) / smoothened_true_range
    DI_pos = (smoothened_DM_pos * 100) / smoothened_true_range

    ADX = DX.rolling(smoothen_window).mean()
    return DI_pos, DI_neg, ADX, ADX
