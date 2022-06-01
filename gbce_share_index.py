import pandas as pd
import numpy as np
from trades import Trade, TradeLog
from datetime import datetime, timedelta


# 1b)
def generate_random_trades(stocks_db_path: str = './stock_sample_data.csv') -> list:
    stocks_info = pd.read_csv(stocks_db_path, index_col='Stock Symbol')
    stock_symbols = stocks_info.index.array
    trades = []
    for i in range(0, stock_symbols.size):
        new_trade = Trade(stock_symbols[i], datetime.now() + timedelta(-1 * np.random.randint(1, 20)), np.random.randint(1, 100), np.random.choice(['BUY', 'SELL']), np.random.randint(1, 100))
        trades.append(new_trade)

    return trades


def geometric_mean(x) -> float:
    a = np.log(x)
    return np.exp(a.mean())


def calculate_gbce_index_of_stocks(trades: list) -> float:
    prices = []
    for trade in trades:
        prices.append(trade.traded_price)

    return geometric_mean(sum(prices))


# Just testing functions
if __name__ == '__main__':
    trades = generate_random_trades()
    tradeLog = TradeLog(trades)
    volume_weighted_average = tradeLog.volume_weighted_stock_price_15_min
    gbce_index_of_stocks = calculate_gbce_index_of_stocks(trades)

