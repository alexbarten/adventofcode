from day01.reportrepair_0 import find_entries_of_sum, multiply_entries


def test_find_entries_of_sum():
    result = find_entries_of_sum(2020, 'tests/entries_0.txt')
    assert result == [1721, 299]


def test_multiply_entries():
    result = multiply_entries(1721, 299)
    assert result == 514579
