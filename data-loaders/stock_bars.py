# python stock_bars.py TICKER INTERVAL LENGTH
# TICKER: SPY or AAPL for example
# INTERVAL: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, or 3mo
# LENGTH: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max

import yfinance as yf
import sys
from pathlib import Path

argc = len(sys.argv)

if argc < 4:
    print('Not enough args, see source')
    sys.exit(1)

ticker = sys.argv[1]
interval = sys.argv[2]
length = sys.argv[3]

df = yf.download(tickers=ticker, period=length, interval=interval)

df.rename(
    columns={
        'Open': 'open',
        'High': 'high',
        'Low': 'low',
        'Close': 'close',
        'Volume': 'volume',
        'Adj Close': 'adj_close'
    }, inplace=True, errors='raise'
)
df.index.names = ['date']

base_path = Path(__file__).parent / '..'
df.to_csv(base_path / 'data/yfinance/{}_{}_{}.csv'.format(ticker, interval, length))
