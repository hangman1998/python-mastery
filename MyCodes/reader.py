import csv
from typing import Callable
import collections


def read_csv_as_dicts(filename: str, column_types: list[Callable]) -> list[dict]:
    with open(filename) as f:
        csv_f = csv.reader(f)
        heading = next(csv_f)
        records = [
            {name: type(data) for name, type, data in zip(heading, column_types, row)}
            for row in csv_f
        ]
        return records


class DataCollection(collections.abc.Sequence):
    def __init__(self, data_store: dict[str, list]):
        self.data_store = data_store
        self.column_names = list(data_store.keys())

    def __len__(self):
        # All lists assumed to have the same length
        return len(self.data_store[self.column_names[0]])

    def __getitem__(self, index):
        if isinstance(index, slice):
            return DataCollection(
                {col: self.data_store[col][index] for col in self.column_names}
            )
        else:
            return {col: self.data_store[col][index] for col in self.column_names}

    def append(self, d):
        for col in self.column_names:
            self.data_store[col].append(d[col])


def read_csv_as_columns(filename: str, column_types: list[Callable]) -> list[dict]:
    with open(filename) as f:
        csv_f = csv.reader(f)
        heading = next(csv_f)
        records = DataCollection({col: [] for col in heading})
        for row in csv_f:
            record = {
                name: type(value)
                for name, type, value in zip(heading, column_types, row)
            }
            records.append(record)
        return records
