from backtester import backtest
import pandas as pd
import sys

data_path = 'data/binance/BTCUSDT_15m_1-Jan-2019_1-Jan-2020.csv'
df = pd.read_csv(data_path)

backtest(lambda x:x, df)
