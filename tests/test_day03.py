import pytest
from solutions.day03 import solve

def test_day01():
    expected_part1 = 161
    expected_part2 = 48
    assert solve() == (expected_part1, expected_part2)