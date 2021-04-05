import sys
sys.path.append('..')
from backtester.backtester import backtest
import numpy as np
import pandas as pd
import sys
from matplotlib import pyplot as plt
from util.metrics import sharpe_ratio

def example_backtest(name, strategy, parameters, df):
    price = df['close'].to_numpy()
    normalized_price = price / price[0]

    fee = 0.001

    returns = backtest(strategy, parameters, df, 0)
    returns_after_fees = backtest(strategy, parameters, df, fee)
    buy_and_hold_returns = np.concatenate(([1 - fee], price[1:] / price[:-1]))

    print('sharpe ratio:', sharpe_ratio(returns_after_fees / buy_and_hold_returns, len(price)))

    plt.plot(normalized_price, label='Buy and Hold')
    plt.plot(np.cumprod(returns), label=name + ' (no fees)')
    plt.plot(np.cumprod(returns_after_fees), label=name + ' (with %s%% fees)' % (fee * 100))
    plt.title(name)
    plt.xlabel('Candles Elapsed')
    plt.ylabel('Dollar Multiplier')
    plt.legend()
    plt.savefig('../plots/' + name + '.png')
    plt.show()
