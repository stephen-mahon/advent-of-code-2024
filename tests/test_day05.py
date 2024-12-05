import pytest
from solutions.day05 import solve

def test_day01():
    expected_part1 = 143
    expected_part2 = 123
    assert solve() == (expected_part1, expected_part2)