from .indicators.EXAMPLE_SMA import SMA

def strategy(history, state, parameters):
    if len(history) >= parameters['slow']:
        lookback = history.tail(parameters['slow'])['close'].to_numpy()
        MACD = SMA(lookback, parameters['fast']) - SMA(lookback, parameters['slow'])
        return {
            'allocation': 1 if MACD > 0 else 0
        }
    return {
        'allocation': 0
    }

