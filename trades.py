from dataclasses import dataclass, field
from typing import List
from datetime import datetime, timedelta
import numpy as np


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
    trades: List[Trade] = field(default_factory=lambda: [])

    def log_trade(self, trade: Trade):
        self.trades.append(trade)

    def volume_weighted_stock_price_15_min(self, symbol: str) -> float:
        trades_with_symbol = [trade for trade in self.trades if trade.stock_symbol == symbol]

        if len(trades_with_symbol) == 0:
            return -1

        timestamp_15_mins_ago = datetime.now() - timedelta(minutes=15)
        trades_in_last_15_mins = [trade for trade in trades_with_symbol if trade.timestamp >= timestamp_15_mins_ago]
        traded_prices_in_last_15_mins = [trade.traded_price for trade in trades_in_last_15_mins]
        volume_of_trades_in_last_15_mins = [trade.num_shares for trade in trades_in_last_15_mins]
        
        pennies_traded = np.dot(
            traded_prices_in_last_15_mins,
            volume_of_trades_in_last_15_mins
        )

        return pennies_traded / sum(volume_of_trades_in_last_15_mins)

