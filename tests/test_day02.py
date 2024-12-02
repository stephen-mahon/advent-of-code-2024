import pytest
from solutions.day02 import solve

def test_day01():
    expected_part1 = 2
    expected_part2 = 4
    assert solve() == (expected_part1, expected_part2)
