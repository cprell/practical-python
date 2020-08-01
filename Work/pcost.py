# pcost.py

import csv
import sys


def portfolio_cost(filename):
    total_cost = 0.0
    f = open(filename, 'rt')
    rows = csv.reader(f)
    next(rows)
    for row in rows:
        print(row)
        try:
            shares = int(row[1])
            price = float(row[2])
            total_cost = total_cost + shares * price
        except ValueError:
            print("Couldn't parse", row)

    f.close()
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'


cost = portfolio_cost(filename)
print('Total cost', cost)
