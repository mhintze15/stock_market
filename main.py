from stocks import calculate_dividend_yield, calculate_p_e_ratio
from trades import Trade, TradeLog
from datetime import datetime, timedelta

if __name__ == '__main__':
    dividend_yield = calculate_dividend_yield(
        symbol='POP',
        price=5.32,
    )

    PE = calculate_p_e_ratio(
        symbol='GIN',
        price=5.32,
    )

    trade_too_early = Trade(
        stock_symbol='META',
        timestamp=datetime.now() - timedelta(minutes=40),
        num_shares=55,
        direction='BUY',
        traded_price=1000
    )

    trade_1 = Trade(
        stock_symbol='META',
        timestamp=datetime.now() - timedelta(minutes=4),
        num_shares=100,
        direction='BUY',
        traded_price=100
    )
    trade_2 = Trade(
        stock_symbol='TSLA',
        timestamp=datetime.now() - timedelta(minutes=2),
        num_shares=100,
        direction='BUY',
        traded_price=430
    )

    trade_3 = Trade(
        stock_symbol='META',
        timestamp=datetime.now() - timedelta(minutes=1),
        num_shares=100,
        direction='BUY',
        traded_price=90
    )

    tl = TradeLog()

    tl.log_trade(trade_too_early)
    tl.log_trade(trade_1)
    tl.log_trade(trade_2)
    tl.log_trade(trade_3)

    assert(tl.volume_weighted_stock_price_15_min(symbol='META') == 95)
