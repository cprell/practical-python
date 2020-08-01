# pcost.py


def portfolio_cost(filename):
    total_cost = 0.0
    f = open(filename, 'rt')
    next(f)
    for line in f:
        row = line.split(',')
        total_cost = total_cost + int(row[1]) * float(row[2])
    return total_cost


cost = portfolio_cost('Data/portfolio.csv')
print('Total cost', cost)
