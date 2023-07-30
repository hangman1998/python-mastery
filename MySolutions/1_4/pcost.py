def stock_value(line: str) -> float:
    _, shares, price = line.split()
    try:
        shares = int(shares)
        price = float(price)
        return shares * price
    except ValueError as e:
        print("Couldn't parse:", repr(line))
        print("Reason:", e)
        # warnings.warn(f"Couldn't parse: {repr(line)}\nReason: {e}")
        return 0


def portfolio_cost(filename: str) -> float:
    with open(filename) as portfolio_file:
        stock_values = (stock_value(line) for line in portfolio_file)
        total_cost = sum(stock_values)
        return total_cost


print(portfolio_cost("Data/portfolio3.dat"))
