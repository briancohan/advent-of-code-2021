import day_01

test_data = """
199
200
208
210
200
207
240
269
260
263
"""


def test_data_read_as_numbers():
    given = day_01.read_data(test_data)
    expected = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert given == expected


def test_correct_number_of_increases():
    data = day_01.read_data(test_data)
    given = day_01.count_increases(data)
    expected = 7
    assert given == expected


def test_data_averaged_correctly():
    data = day_01.read_data(test_data)
    given = day_01.average_data(data)
    expected = [607, 618, 618, 617, 647, 716, 769, 792]
    assert given == expected
