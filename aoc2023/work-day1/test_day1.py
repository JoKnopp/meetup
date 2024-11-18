import day1

def test_part1() -> None:
    # task description:
    with open("data/test_part1.txt") as f:
        test_data = list(day1.read_input(f))
    calibration_values = [12, 38, 15, 77]
    total = 142

    results = []
    for line in test_data:
        d1, d2 = day1.find_first_and_last_digit(line)
        results.append(day1.digits_to_number(d1, d2))
    assert calibration_values == results
    assert sum(calibration_values) == total == day1.compute_result(test_data)
