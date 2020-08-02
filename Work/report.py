# report.py
#
# Exercise 2.4

import csv


def read_portfolio(filename):
    """ Computes the total cost (shares*price) of a portfolio file """
    output_portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            record = dict(zip(header, row))
            stock = {
                'name': record['name'],
                'shares': int(record['shares']),
                'price': float(record['price'])
            }
            output_portfolio.append(stock)

    return output_portfolio


def read_prices(filename):
    """ reads prices from a file """
    output_prices = {}

    f = open(filename, 'r')
    rows = csv.reader(f)
    for row in rows:
        try:
            output_prices[row[0]] = float(row[1])
            print(row)
        except IndexError:
            pass

    return output_prices


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

total_portfolio_sum = 0.0
for s in portfolio:
    total_portfolio_sum += s['shares'] * s['price']

print('Total Cost', total_portfolio_sum)

current_prices_sum = 0.0
for s in portfolio:
    current_prices_sum += s['shares'] * prices[s['name']]

print('Total value', current_prices_sum)
print('Total gain', round(total_portfolio_sum - current_prices_sum, 2))


def make_report():
    report = []
    report_portfolio = read_portfolio('Data/portfoliodate.csv')
    report_price = read_prices('Data/prices.csv')
    for s in report_portfolio:
        change = report_price[s['name']] - s['price']
        report.append((s['name'], s['shares'], report_price[s['name']], change))

    print_report(report)


def print_report(report):
    print_header()
    currency = '$'
    for name, shares, price, change in report:
        price_with_currency = currency + str(price)
        print(f'{name:>10s} {shares:>10d} {price_with_currency:>10} {change:>10.2f}')


def print_header():
    headers = ('Name', 'Shares', 'Price', 'Change')
    header_underline = '----------'
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(' '.join([header_underline]*len(headers)))