from stocks import calculate_dividend_yield, calculate_p_e_ratio

# Testing functions
if __name__ == '__main__':
    dividend_yield = calculate_dividend_yield(
        symbol='POP',
        price=5.32,
    )

    PE = calculate_p_e_ratio(
        symbol='GIN',
        price=5.32,
    )
