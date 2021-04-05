import numpy as np

def sharpe_ratio(returns, periods_per_year):
    return np.sqrt(periods_per_year) * (np.mean(returns) - 1) / np.std(returns)
