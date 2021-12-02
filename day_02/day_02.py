from pathlib import Path


def read_data(data: str) -> list[tuple[str, int]]:
    _data = []
    for line in data.splitlines():
        if not line:
            continue
        direction, distance = line.split()
        _data.append((direction, int(distance)))
    return _data


def final_position(
    data: list[tuple[str, int]], track_aim: bool = False
) -> tuple[int, int]:
    horiz_pos = 0
    vert_pos = 0
    aim = 0

    for direction, distance in data:
        if direction == "forward":
            if track_aim:
                vert_pos += distance * aim
            horiz_pos += distance
        elif direction == "up":
            if track_aim:
                aim -= distance
            else:
                vert_pos -= distance
        elif direction == "down":
            if track_aim:
                aim += distance
            else:
                vert_pos += distance
    return horiz_pos, vert_pos


def part_1(raw_data: str):
    data = read_data(raw_data)
    horiz_pos, vert_pos = final_position(data)
    print(horiz_pos * vert_pos)


def part_2(raw_data: str):
    data = read_data(raw_data)
    horiz_pos, vert_pos = final_position(data, track_aim=True)
    print(horiz_pos * vert_pos)


if __name__ == "__main__":
    raw_data = Path("input.txt").read_text()
    part_1(raw_data)
    part_2(raw_data)
