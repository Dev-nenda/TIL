# reader.py

import csv

def read_csv_as_dicts(filename, types):
    '''
    Read a CSV file into a list of dicts with column type conversion
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = { name: func(val) for name, func, val in zip(headers, types, row) }
            records.append(record)
    return records

def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records


# stock.py

class Stock:
    types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

def read_portfolio(filename):
    '''
    Read a CSV file of stock data into a list of Stocks
    '''
    import csv
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = Stock.from_row(row)
            portfolio.append(record)
    return portfolio

if __name__ == '__main__':
    import tableformat
    import reader
    # portfolio = read_portfolio('../../Data/portfolio.csv')
    portfolio = reader.read_csv_as_instances('../../Data/portfolio.csv', Stock)
    tableformat.print_table(portfolio, ['name', 'shares', 'price'])

# tableformat.py

# Print a table
def print_table(records, fields):
    # Print the table headers in a 10-character wide field
    for fieldname in fields:
        print('%10s' % fieldname, end=' ')
    print()

    # Print the separator bars
    print(('-'*10 + ' ')*len(fields))

    # Output the table contents
    for r in records:
        for fieldname in fields:
            print('%10s' % getattr(r, fieldname), end=' ')
        print()


