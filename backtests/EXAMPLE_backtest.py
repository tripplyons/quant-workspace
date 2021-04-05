import sys
sys.path.append('..')
from backtester.backtester import backtest
import numpy as np
import pandas as pd
import sys
from matplotlib import pyplot as plt
from util.metrics import sharpe_ratio

from strategies.EXAMPLE_MACD import strategy

df = pd.read_csv('../data/binance/EXAMPLE_BTCUSDT_1h_1-Jan-2019_1-Jan-2020.csv')

price = df['close'].to_numpy()
normalized_price = price / price[0]

parameters = {
    'slow': 26,
    'fast': 12
}

fee = 0.001

returns = backtest(strategy, parameters, df, 0)
returns_after_fees = backtest(strategy, parameters, df, fee)
buy_and_hold_returns = np.concatenate(([1 - fee], price[1:] / price[:-1]))

print('sharpe ratio:', sharpe_ratio(returns_after_fees / buy_and_hold_returns, len(price)))

plt.plot(normalized_price, label='Bitcoin in 2019')
plt.plot(np.cumprod(returns), label='MACD Strategy (no fees)')
plt.plot(np.cumprod(returns_after_fees), label='MACD Strategy (with %s%% fees)' % (fee * 100))
plt.title('MACD Strategy')
plt.xlabel('15 Minute Candles Elapsed')
plt.ylabel('Dollar Multiplier')
plt.legend()
plt.savefig('../plots/EXAMPLE_MACD_returns.png')
plt.show()
