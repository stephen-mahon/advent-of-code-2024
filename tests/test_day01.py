import pytest
from solutions.day01 import solve

def test_day01():
    expected_part1 = 11
    expected_part2 = 31
    assert solve() == (expected_part1, expected_part2)
