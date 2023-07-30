with open("Data/portfolio.dat") as portfolio_data:
    table = (row.split() for row in portfolio_data)
    stock_values = (float(row[1]) * float(row[2]) for row in table)
    total_cost = sum(stock_values)
    print("total portfolio cost is: ", total_cost)
