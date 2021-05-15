import numpy as np
import pandas as pd
from yahoo_financial_data_module import Ticker

ticker = Ticker('INFY.NS')
ticker_data = ticker.get_historical_stock_price()

def series_smoothener(series, smoothen_window = 14):
    init_smoothener = np.zeros(smoothen_window - 1)
    smoothen_series = np.zeros(len(series) - (smoothen_window - 1))
    smoothen_series[0] = series.dropna()[0 : smoothen_window].sum()
    indices = series.index.tolist()
    series = series.tolist()
    for i in range(1, len(smoothen_series) - 1):
        smoothen_series[i] = (smoothen_series[i - 1] - (smoothen_series[i - 1] / float(smoothen_window)) + series[smoothen_window + i])
    return smoothen_series

def ADX_indicator(df, smoothen_period = 14):
    diff_directional_index = (pd.DataFrame([df['close'].shift(1),df['high']]).max(axis=0,skipna=False) - 
                            pd.DataFrame([df['close'].shift(1),df['low']]).min(axis=0,skipna=False))
    diff_directional_index = series_smoothener(diff_directional_index)
    
    diff_up = df['high'] - df['high'].shift(1)
    diff_down = df['low'].shift(1) - df['low']
    
    di_pos = series_smoothener(diff_up.where(np.logical_or(np.logical_and(diff_up > diff_down, diff_up > 0), diff_up.isnull()),0))
    di_neg = series_smoothener(diff_down.where(np.logical_or(np.logical_and(diff_down > diff_up, diff_down > 0), diff_down.isnull()),0))
    
    di_pos = 100 * di_pos/diff_directional_index
    di_neg = 100 * di_neg/diff_directional_index
    
    DX = 100 * pd.Series((di_pos - di_neg) / (di_pos + di_neg)).abs()
    
    ADX = np.zeros(len(diff_directional_index))
    
    ADX[smoothen_period] = DX[0 : smoothen_period].mean()

    for i in range(smoothen_period + 1, len(ADX)):
        ADX[i] = ((ADX[i - 1] * (smoothen_period - 1)) + DX[i - 1]) / float(smoothen_period)

    df['DI_positive'] = np.concatenate([np.zeros(smoothen_period - 1),di_pos])
    df['DI_negative'] = np.concatenate([np.zeros(smoothen_period - 1),di_neg])
    df['ADX'] = np.concatenate([np.zeros(smoothen_period - 1),ADX])
    return df

ticker_data = ADX_indicator(ticker_data)