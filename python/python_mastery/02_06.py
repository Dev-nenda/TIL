# colreader.py

import collections
import csv

class DataCollection(collections.abc.Sequence):
    def __init__(self, columns):
        self.column_names = list(columns)
        self.column_data = list(columns.values())

    def __len__(self):
        return len(self.column_data[0])

    def __getitem__(self, index):
        return dict(zip(self.column_names,
                        (col[index] for col in self.column_data)))


def read_csv_as_columns(filename, types):
    columns = collections.defaultdict(list)
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            for name, func, val in zip(headers, types, row):
                columns[name].append(func(val))
            
    return DataCollection(columns)

if __name__ == '__main__':
    import tracemalloc
    from sys import intern

    tracemalloc.start()
    data = read_csv_as_columns('../../Data/ctabus.csv', [intern, intern, intern, int])
    print(tracemalloc.get_traced_memory())



# cta.py

from collections import defaultdict, Counter
import tracemalloc
import csv
import sys

tracemalloc.start()

if True:
    # Part (b)
    import reader
    rows = reader.read_csv_as_dicts('../../Data/ctabus.csv',
                                    [sys.intern, sys.intern, sys.intern, int])
else:
    # Part (d) - Challenge
    import colreader
    rows = colreader.read_csv_as_columns('../../Data/ctabus.csv', 
                                         [sys.intern, sys.intern, sys.intern, int])

# --------------------------------------------------
# Question 1:  How many bus routes are in Chicago?
# Solution: Use a set to get unique values. 

routes = set()
for row in rows:
    routes.add(row['route'])
print(len(routes), 'routes')

# --------------------------------------------------
# Question 2: Total number of rides per route
# Solution: Use a counter to tabulate things
rides_per_route = Counter()
for row in rows:
    rides_per_route[row['route']] += row['rides']

# Make a table showing the routes and a count ranked by popularity
for route, count in rides_per_route.most_common():
    print('%5s %10d' % (route, count))

# --------------------------------------------------
# Question 3: Routes with greatest increase in ridership 2001 - 2011
# Solution: Counters embedded inside a defaultdict

rides_by_year = defaultdict(Counter)
for row in rows:
    year = row['date'].split('/')[2]
    rides_by_year[year][row['route']] += row['rides']

diffs = rides_by_year['2011'] - rides_by_year['2001']
for route, diff in diffs.most_common(5):
    print(route, diff)

# ---- Memory use
print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())


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

        

    


