def backtest(strategy, data, fee=0):
    state = {
        # 0 for not owning the asset, 1 for all in on the asset
        'allocation': 0
    }

    print(data.head(100)['close'])

    # for time in range(len(data)):
    #     oldState = state
    #     state = strategy(data.head(time), state)