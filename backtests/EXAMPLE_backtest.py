import sys
sys.path.append('..')
from backtester.backtester import backtest
import numpy as np
import pandas as pd
import sys
from matplotlib import pyplot as plt

from strategies.EXAMPLE_MACD import strategy

df = pd.read_csv('../data/binance/EXAMPLE_BTCUSDT_1h_1-Jan-2019_1-Jan-2020.csv')

price = df['close'].to_numpy()
returns = backtest(strategy, df)
fee = 0.001
returns_after_fees = backtest(strategy, df, fee)

plt.plot(price / price[0], label='Bitcoin in 2019')
plt.plot(np.cumprod(returns), label='MACD Strategy (no fees)')
plt.plot(np.cumprod(returns_after_fees), label='MACD Strategy (with %s%% fees)' % (fee * 100))
plt.legend()
plt.savefig('../plots/EXAMPLE_MACD_returns.png')
plt.show()
