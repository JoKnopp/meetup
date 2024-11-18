import day1
import pytest


@pytest.mark.parametrize("digit_finder", day1.DIGIT_FINDER_BY_NAME.values())
def test_find_last_num(digit_finder) -> None:
    # don't be confused by overlapping words
    test_data = ["oneoneight"]
    calibration_values = [18]
    total = 18

    results = []
    for line in test_data:
        d1, d2 = day1.find_first_and_last_digit(line, digit_finder=digit_finder)
        results.append(day1.digits_to_number(d1, d2))
    assert calibration_values == results
    assert (
        sum(calibration_values)
        == total
        == day1.compute_result(test_data, digit_finder=digit_finder)
    )


@pytest.mark.parametrize("digit_finder", day1.DIGIT_FINDER_BY_NAME.values())
def test_part1(digit_finder) -> None:
    # task description:
    with open("data/test_part1.txt") as f:
        test_data = list(day1.read_input(f))
    calibration_values = [12, 38, 15, 77]
    total = 142

    results = []
    for line in test_data:
        d1, d2 = day1.find_first_and_last_digit(line, digit_finder=digit_finder)
        results.append(day1.digits_to_number(d1, d2))
    assert calibration_values == results
    assert sum(calibration_values) == total == day1.compute_result(test_data)


@pytest.mark.parametrize("digit_finder", day1.DIGIT_FINDER_BY_NAME.values())
def test_part2(digit_finder) -> None:
    with open("data/test_part2.txt") as f:
        test_data = list(day1.read_input(f))
    calibration_values = [29, 83, 13, 24, 42, 14, 76]
    total = 281

    results = []
    for line in test_data:
        d1, d2 = day1.find_first_and_last_digit(line, digit_finder=digit_finder)
        results.append(day1.digits_to_number(d1, d2))
    assert calibration_values == results
    assert sum(calibration_values) == total == day1.compute_result(test_data)
