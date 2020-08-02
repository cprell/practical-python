# pcost.py

import csv
import sys


def portfolio_cost(filename):
    total_cost = 0.0
    f = open(filename, 'rt')
    rows = csv.reader(f)
    header = next(rows)
    for rowno, row in enumerate(rows, start=1):
        record = dict(zip(header, row))
        print(row)
        try:
            shares = int(record['shares'])
            price = float(record['price'])
            total_cost = total_cost + shares * price
        except ValueError:
            print(f'Row {rowno}: Bad row: {row}')

    f.close()
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'


cost = portfolio_cost(filename)
print('Total cost', cost)
