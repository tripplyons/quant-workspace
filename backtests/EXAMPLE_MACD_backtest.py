from EXAMPLE_backtest import example_backtest
from strategies.EXAMPLE_MACD import strategy
import pandas as pd

df = pd.read_csv('../data/binance/EXAMPLE_BTCUSDT_1h_1-Jan-2019_1-Jan-2020.csv')

parameters = {
    'slow': 26,
    'fast': 12
}

example_backtest('EXAMPLE_MACD', strategy, parameters, df)
