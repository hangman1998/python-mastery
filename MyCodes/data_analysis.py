import csv
from collections import Counter
from pprint import pprint
from typing import Callable


def read_csv(filename: str) -> list[dict]:
    """
    turning a csv file into a generator that turns each row into a {column: value} dict.
    """
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            record = dict(zip(headings, row))
            yield record


if __name__ == "__main__":
    # How many bus routes exist in Chicago?

    bus_routes = {row["route"] for row in read_csv("Data/ctabus.csv")}
    print(f"there are {len(bus_routes)} bus routes in chicago")
    # How many people rode the number 22 bus on February 2, 2011? What about any route on any date of your choosing?
    select_rides = lambda route, date: next(
        int(row["rides"])
        for row in read_csv("Data/ctabus.csv")
        if row["date"] == date and row["route"] == route
    )
    print(
        f"{select_rides('22','02/02/2011')} many people rode on route 22 on February 2, 2011"
    )
    bus_routes_total_rides = Counter(
        {row["route"]: int(row["rides"]) for row in read_csv("Data/ctabus.csv")}
    )
    # What is the total number of rides taken on each bus route?
    # pprint(bus_routes_total_rides)
    # What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?
    year: Callable[[str], str] = lambda date: date.split("/")[-1]

    bus_routes_total_rides_2001 = Counter(
        {
            row["route"]: int(row["rides"])
            for row in read_csv("Data/ctabus.csv")
            if year(row["date"]) == "2001"
        }
    )

    bus_routes_total_rides_2011 = Counter(
        {
            row["route"]: int(row["rides"])
            for row in read_csv("Data/ctabus.csv")
            if year(row["date"]) == "2011"
        }
    )
    bust_routes_total_rides_inc = (
        bus_routes_total_rides_2011 - bus_routes_total_rides_2001
    )
    pprint(bust_routes_total_rides_inc.most_common(5))
