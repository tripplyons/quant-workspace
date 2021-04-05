import numpy as np

def SMA(series, length):
    return np.mean(series[-length:])
