import day1
import pytest


@pytest.mark.parametrize(
    "fname,calibration_values",
    [
        pytest.param("data/test_part1.txt", [12, 38, 15, 77], id="part1"),
        pytest.param("data/test_part2.txt", [29, 83, 13, 24, 42, 14, 76], id="part2"),
        pytest.param("data/test_find_last_num.txt", [18], id="find_last_num"),
    ],
)
@pytest.mark.parametrize("digit_finder", day1.DIGIT_FINDER_BY_NAME.values())
def test_day1(fname, calibration_values, digit_finder) -> None:
    with open(fname) as f:
        test_data = list(day1.read_input(f))

    results = list(day1.process_lines(test_data, digit_finder=digit_finder))
    assert calibration_values == results
