from pathlib import Path


def read_data(data: str) -> list[list[int]]:
    """Convert text file to list of lists of type integer."""
    return [[int(i) for i in line.strip()] for line in data.strip().splitlines()]


def most_common_bit(digits: list[int]) -> int:
    """Find the most common digit in the list.

    List is assumed to be a list of 0s and 1s.
    If there is a tie, return -1.
    """
    ones = sum(digits)
    zeros = len(digits) - ones
    if ones > zeros:
        return 1
    elif zeros > ones:
        return 0
    else:
        return -1


def get_digits(
    data: list[list[int]],
    gamma: bool = True,
) -> list[int]:
    """Get the most prevalent digit in each column.

    if gamma is false, each bit is inverted
    """
    digits = [most_common_bit([row[ix] for row in data]) for ix in range(len(data[0]))]
    favor = 1 if gamma else 0
    digits = [favor if digit == -1 else digit for digit in digits]
    if not gamma:
        digits = [1 - digit for digit in digits]
    return digits


def scrubber_rating(data: list[list[int]], oxy: bool = True) -> list[int]:
    """Calculate the rating of a scrubber.

    if oxy is true, keep the records with the most common digit in each subsequent column
    if oxy is false, keep the records with the least common digit in each subsequent column
    """
    for ix in range(len(data[0])):
        digits = [row[ix] for row in data]
        most_common = abs(most_common_bit(digits))
        keep = 1 if oxy == most_common else 0
        data = [row for row in data if row[ix] == keep]

        if len(data) == 1:
            return data[0]


def decode_digits(digits: list[int]) -> int:
    """Decode a list of binary digits to an integer."""
    return int("".join([str(i) for i in digits]), 2)


def part_1(raw_data: str):
    data = read_data(raw_data)
    g = get_digits(data, gamma=True)
    e = get_digits(data, gamma=False)
    print(decode_digits(g) * decode_digits(e))


def part_2(raw_data: str):
    data = read_data(raw_data)
    oxy = scrubber_rating(data, oxy=True)
    co2 = scrubber_rating(data, oxy=False)
    print(decode_digits(oxy) * decode_digits(co2))


if __name__ == "__main__":
    raw_data = Path("puzzle_data.txt").read_text()
    part_1(raw_data)
    part_2(raw_data)
