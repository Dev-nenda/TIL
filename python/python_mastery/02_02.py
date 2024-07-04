# cta.py

from collections import defaultdict, Counter
import tracemalloc
import readrides

tracemalloc.start()

rows = readrides.read_rides_as_dicts('../../Data/ctabus.csv')

# --------------------------------------------------
# Question 1:  How many bus routes are in Chicago?
# Solution: Use a set to get unique values. 

routes = set()
for row in rows:
    routes.add(row['route'])
print(len(routes), 'routes')

# --------------------------------------------------
# Question 2: How many people rode route 22 on February 2, 2011?
# Solution: Make dictionary with composite keys

by_route_date = { }
for row in rows:
    by_route_date[row['route'], row['date']] = row['rides']

print('Rides on Route 22, February 2, 2011:', by_route_date['22','02/02/2011'])

# --------------------------------------------------
# Question 3: Total number of rides per route
# Solution: Use a counter to tabulate things
rides_per_route = Counter()
for row in rows:
    rides_per_route[row['route']] += row['rides']

# Make a table showing the routes and a count ranked by popularity
for route, count in rides_per_route.most_common():
    print('%5s %10d' % (route, count))

# --------------------------------------------------
# Question 4: Routes with greatest increase in ridership 2001 - 2011
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


# readport.py

import csv

# A function that reads a file into a list of dicts
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {
                'name' : row[0],
                'shares' : int(row[1]),
                'price' : float(row[2])
                }
            portfolio.append(record)
    return portfolio

# readrides.py

import csv

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of dicts
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route, 
                'date': date, 
                'daytype': daytype, 
                'rides' : rides
                }
            records.append(record)
    return records

class Row:
    # Uncomment to see effect of slots
    # __slots__ = ('route', 'date', 'daytype', 'rides')
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

# Uncomment to use a namedtuple instead
#from collections import namedtuple
#Row = namedtuple('Row',('route','date','daytype','rides'))

def read_rides_as_instances(filename):
    '''
    Read the bus ride data as a list of instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    read_rides = read_rides_as_tuples # Change to as_dicts, as_instances, etc.
    rides = read_rides("../../Data/ctabus.csv")

    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
