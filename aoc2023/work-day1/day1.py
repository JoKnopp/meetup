#!/usr/bin/env python3
from typing import Iterator, Iterable


def read_input(fname: str) -> Iterator[str]:
    with open(fname) as f:
        for line in f:
            yield line


def find_first_and_last_digit(line: str) -> tuple[int, int]:
    first_digit: int = None
    last_digit: int = None
    for c in line:
        if c.isdigit():
            if first_digit is None:
                first_digit = c
            else:
                last_digit = c
    # only one digit on the line means it is the first and last digit
    if last_digit is None:
        last_digit = first_digit
    return first_digit, last_digit


def digits_to_number(digit1: str, digit2: str) -> int:
    return int(f"{digit1}{digit2}")


def compute_result(lines: Iterable) -> int:
    result = 0
    for line in lines:
        d1, d2 = find_first_and_last_digit(line)
        result += digits_to_number(d1, d2)
    return result


def cli() -> None:
    print(
        compute_result(read_input("data/input.txt"))
    )


if __name__ == "__main__":
    cli()
