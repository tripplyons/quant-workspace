import numpy as np

def SMA(series, length):
    # print(series)
    return np.mean(series[-length:])
