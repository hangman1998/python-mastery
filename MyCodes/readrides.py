import csv
from collections import namedtuple


class RowClass:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


RowNamedTuple = namedtuple("RowNamedTuple", ["route", "date", "daytype", "rides"])


class RowClassWithSlots:
    __slots__ = ["route", "date", "daytype", "rides"]

    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_rides(filename: str, method: str):
    """
    Read the bus ride data as a list of tuples
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            if method == "TUPLE":
                record = (route, date, daytype, rides)
            elif method == "DICT":
                record = {
                    "route": route,
                    "date": date,
                    "daytype": daytype,
                    "rides": rides,
                }
            elif method == "CLASS":
                record = RowClass(route, date, daytype, rides)
            elif method == "NAMED_TUPLE":
                record = RowNamedTuple(route, date, daytype, rides)
            elif method == "SLOTS":
                record = RowClassWithSlots(route, date, daytype, rides)
            records.append(record)
    return records


if __name__ == "__main__":
    import tracemalloc

    method = "SLOTS"
    tracemalloc.start()
    rows = read_rides("Data/ctabus.csv", method)
    current, peak = tracemalloc.get_traced_memory()
    print(
        f"method {method} Memory Use: Current {current/1000000:0.2f} MB, Peak {peak/1000000:0.2f} MB"
    )
