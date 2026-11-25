"""Part 10: your own tests for parse_walk. The README says what to write here.

We grade this file by running it against a correct walks.py, where every test must pass,
and against versions of walks.py with a bug planted in parse_walk, where your tests should fail.
"""

import pytest

from walks import Walk, parse_walk


@pytest.fixture
def good_row() -> dict[str, str]:
    """Provided: one good row, as csv.DictReader gives it. Each test gets its own new copy."""
    return {"date": "2026-11-16", "steps": "4200", "place": "Lumphini Park"}


def test_core_example_a_good_row_becomes_a_walk(good_row):
    """Provided: an example that uses the fixture. Write your own tests below it."""
    assert parse_walk(good_row) == Walk("2026-11-16", 4200, "Lumphini Park")


# Your tests go here.
def test_strips_whitespace_around_fields(good_row):
    good_row["date"] = "  2026-11-16  "
    good_row["steps"] = "  4200  "
    good_row["place"] = "  Lumphini Park  "
    assert parse_walk(good_row) == Walk("2026-11-16", 4200, "Lumphini Park")

def test_zero_steps_is_allowed(good_row):
    good_row["steps"] = "0"
    assert parse_walk(good_row) == Walk("2026-11-16", 0, "Lumphini Park")


def test_one_step_is_allowed(good_row):
    good_row["steps"] = "1"
    assert parse_walk(good_row) == Walk("2026-11-16", 1, "Lumphini Park")


@pytest.mark.parametrize(
    ("field", "bad_value"),
    [
        ("date", ""),
        ("date", "   "),
        ("steps", ""),
        ("steps", "   "),
        ("steps", "-1"),
        ("steps", "-500"),
        ("steps", "abc"),
        ("steps", "42.5"),
        ("place", ""),
        ("place", "   "),
    ],
)
def test_bad_field_values_raise_value_error(good_row, field, bad_value):
    good_row[field] = bad_value
    with pytest.raises(ValueError):
        parse_walk(good_row)