from pathlib import Path
import pytest
import day_03 as aoc

test_data = Path("sample_data.txt").read_text()


def test_data_read_in_correctly():
    given = aoc.read_data(test_data)
    expected = [
        [0, 0, 1, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 1, 1, 0],
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0],
    ]
    print(given)
    assert given == expected


@pytest.mark.parametrize(
    "digits, expected",
    [
        ([0], 0),
        ([1], 1),
        ([0, 1], -1),
        ([0, 0, 1], 0),
        ([1, 1, 0], 1),
    ],
)
def test_finds_most_common_bit(digits, expected):
    given = aoc.most_common_bit(digits)
    assert given == expected


def test_gamma_digits():
    data = aoc.read_data(test_data)
    given = aoc.get_digits(data, gamma=True)
    expected = [1, 0, 1, 1, 0]
    assert given == expected


def test_epsilon_digits():
    data = aoc.read_data(test_data)
    given = aoc.get_digits(data, gamma=False)
    expected = [0, 1, 0, 0, 1]
    assert given == expected


@pytest.mark.parametrize(
    "digits, expected",
    [
        ([1, 0, 1, 1, 0], 22),
        ([0, 1, 0, 0, 1], 9),
    ],
)
def test_decode_digits(digits, expected):
    given = aoc.decode_digits(digits)
    assert given == expected


def test_oxy_scrubber():
    data = aoc.read_data(test_data)
    given = aoc.decode_digits(aoc.scrubber_rating(data, oxy=True))
    expected = 23
    assert given == expected


def test_co2_scrubber():
    data = aoc.read_data(test_data)
    given = aoc.decode_digits(aoc.scrubber_rating(data, oxy=False))
    expected = 10
    assert given == expected
