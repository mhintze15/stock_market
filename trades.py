from dataclasses import dataclass
from typing import List
from datetime import datetime, timedelta


# 1a)iii) and iv)
@dataclass
class Trade:
    stock_symbol: str
    timestamp: datetime
    num_shares: int
    direction: str
    traded_price: float


@dataclass
class TradeLog:
    trades: List[Trade]

    def log_trade(self, trade: Trade):
        self.trades.append(trade)

    @property
    def volume_weighted_stock_price_15_min(self) -> float:
        time = datetime.now() + timedelta(-15)

        traded_price_multiplied_by_quantity = []
        total_shares = []
        for trade in self.trades:
            if time < trade.timestamp < datetime.now():
                traded_price_multiplied_by_quantity.append(trade.traded_price * trade.num_shares)
                total_shares.append(trade.num_shares)

        if sum(total_shares) > 0:
            return sum(traded_price_multiplied_by_quantity) / sum(total_shares)
        else:
            return 0
        