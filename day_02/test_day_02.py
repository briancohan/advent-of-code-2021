import day_02

test_data = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


def test_data_read_in_correctly():
    given = day_02.read_data(test_data)
    expected = [
        ("forward", 5),
        ("down", 5),
        ("forward", 8),
        ("up", 3),
        ("down", 8),
        ("forward", 2),
    ]
    assert given == expected


def test_final_position_correctly_calculated():
    given = day_02.read_data(test_data)
    expected = (15, 10)
    assert day_02.final_position(given) == expected


def test_final_position_correctly_calculated_with_aim():
    given = day_02.read_data(test_data)
    expected = (15, 60)
    assert day_02.final_position(given, track_aim=True) == expected
