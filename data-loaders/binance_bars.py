# python binance_bars.py PAIR INTERVAL START END
# Examples:
# PAIR: BTCUSDT would be Bitcoin / US Dollar Tether
# INTERVAL: 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w (minutes, hours, days, weeks)
# START: '1-Jan-2020' 
# END: Same format as start
from pathlib import Path
import json
from binance.client import Client
import pandas as pd
import sys

argc = len(sys.argv)
if argc < 5:
    print('Not enough args, see source')
    sys.exit(1)

pair = sys.argv[1]
interval = sys.argv[2]
start = sys.argv[3]
end = sys.argv[4]

base_path = Path(__file__).parent / '..'
path = base_path / "keys/data-loader_binance.json"
with path.open() as f:
    keys = json.load(f)


print('logging in...')
bclient = Client(api_key=keys['BINANCE_KEY'], api_secret=keys['BINANCE_SECRET'])

print('downloading...')
klines = bclient.get_historical_klines(pair, interval, start.replace('-', ' '), end.replace('-', ' '))

print('formatting...')
data = pd.DataFrame(klines, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore' ])
# ms to seconds
data['timestamp'] //= 1000
data.set_index('timestamp', inplace=True)

print('saving...')
data.to_csv(base_path / 'data/binance/{}_{}_{}_{}.csv'.format(pair, interval, start, end))
