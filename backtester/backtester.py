import numpy as np

def backtest(strategy, data, fee=0):
    state = {
        # 0 for not owning the asset, 1 for all in on the asset
        'allocation': 0
    }

    returns = [1]

    for time in range(1, len(data)):
        oldState = state
        state = strategy(data.head(time), state)
        allocationChange = np.abs(oldState['allocation'] - state['allocation'])
        priceChange = data['close'][time] / data['close'][time - 1]
        returns.append((1 + state['allocation'] * (priceChange - 1)) - (allocationChange * fee))
    
    return returns