from pathlib import Path


def read_data(data: str) -> list[int]:
    return [int(line) for line in data.strip().splitlines()]


def count_increases(data: list[int]) -> int:
    return sum([1 for a, b in zip(data[:-1], data[1:]) if int(a) - int(b) < 0])


def average_data(data: list[int], window: int = 3) -> list[int]:
    return [sum(data[i : i + window]) for i in range(len(data) - window + 1)]


def part_1(raw_data):
    data = read_data(raw_data)
    print(count_increases(data))


def part_2(raw_data):
    data = average_data(read_data(raw_data))
    print(count_increases(data))


if __name__ == "__main__":
    raw_data = Path("input.txt").read_text()
    part_1(raw_data)
    part_2(raw_data)
