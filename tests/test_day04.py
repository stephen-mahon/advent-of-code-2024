import pytest
from solutions.day04 import solve

def test_day01():
    expected_part1 = 18
    expected_part2 = 9
    assert solve() == (expected_part1, expected_part2)