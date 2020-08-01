# pcost.py


def portfolio_cost(filename):
    total_cost = 0.0
    f = open(filename, 'rt')
    next(f)
    for line in f:
        row = line.split(',')
        try:
            shares = int(row[1])
            price = float(row[2])
        except ValueError:
            print("Couldn't parse", line)
        total_cost = total_cost + shares * price
    return total_cost


cost = portfolio_cost('Data/missing.csv')
print('Total cost', cost)
