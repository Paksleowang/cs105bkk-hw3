"""HW3 · walks.py: read the step counter's CSV file and keep only the good rows. Practises
Session 7 (reading a CSV file, cleaning data) and Session 9 (a generator and a decorator)."""

import csv
from collections.abc import Callable, Iterable, Iterator
from dataclasses import dataclass
from pathlib import Path
from datetime import date


@dataclass
class Walk:
    """Provided: one walk from the log, cleaned. `steps` is a whole number, 0 or more."""

    date: str
    steps: int
    place: str


def parse_walk(row: dict[str, str]) -> Walk:
    """Turn one row of the CSV file into a Walk, or raise ValueError if the row is bad."""
    
    date = row["date"].strip()
    if date == "":
        raise ValueError(f"bad date: {date}")
    steps = int(row["steps"])
    if steps < 0:
        raise ValueError(f"bad steps: {steps}")
    place = row["place"].strip()
    if place == "":
        raise ValueError(f"bad place: {place}")
    return Walk(date, steps, place)
    

def none_on_error(func: Callable) -> Callable:
    """A decorator: the wrapped function returns None instead of raising ValueError."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return None
    return wrapper

def read_rows(path: Path) -> Iterator[dict[str, str]]:
    """Yield the rows of a CSV file one at a time, each as a dict of text."""
    with open(path,"r", newline="") as file:
        text = csv.DictReader(file)
        for row in text:
            yield row

def good_walks(rows: Iterable[dict[str, str]]) -> Iterator[Walk]:
    """Yield a Walk for every good row, one at a time, and skip the bad rows."""
    for row in rows:
        try:
            walk = parse_walk(row)
        except ValueError:
            continue
        if walk is not None:
            yield walk
