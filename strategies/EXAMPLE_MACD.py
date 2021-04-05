from .indicators.EXAMPLE_SMA import SMA

def strategy(history, state):
    lookback = history.tail(26)['close'].to_numpy()
    MACD = SMA(lookback, 12) - SMA(lookback, 26)
    return {
        'allocation': 1 if MACD > 0 else 0
    }
