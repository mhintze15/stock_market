import pandas as pd


# 1a)i)
def calculate_dividend_yield(symbol: str, price: float, stocks_db_path: str = './stock_sample_data.csv') -> float:
    stocks_info = pd.read_csv(stocks_db_path, index_col='Stock Symbol')
    single_stock_info = stocks_info.loc[symbol]

    if single_stock_info['Type'] == 'Common':
        dividend_yield = single_stock_info['Last Dividend'] / price

    elif single_stock_info['Type'] == 'Preferred':
        dividend_yield = (single_stock_info['Fixed Dividend'] * single_stock_info['Par Value']) / price

    else:
        return -1

    return dividend_yield


# 1a)ii)
def calculate_p_e_ratio(symbol: str, price: float, stocks_db_path: str = './stock_sample_data.csv') -> float:
    dividend_yield = calculate_dividend_yield(symbol, price, stocks_db_path)

    return price / dividend_yield
