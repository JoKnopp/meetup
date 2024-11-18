#!/usr/bin/env python3
from typing import Iterator, Iterable, NamedTuple

import click


def read_input(f: click.File) -> Iterator[str]:
    for line in f:
        yield line.rstrip()


class DigitSearchResult(NamedTuple):
    digit: str
    start: int
    end: str


CHARACTERS_TO_DIGIT = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def find_next_digit(text: str, offset: int = 0) -> DigitSearchResult:
    """Returns the next result or None"""
    result = None
    for word, digit in CHARACTERS_TO_DIGIT.items():
        result_start = text[offset:].find(word)
        if result_start != -1:
            start = offset + result_start
            if result is None or start < result.start:
                result = DigitSearchResult(digit=digit, start=start, end=start + len(word))
    return result


def find_first_and_last_digit(line: str) -> tuple[int, int]:
    first_digit_result: DigitSearchResult = find_next_digit(line)
    last_digit_result = first_digit_result
    while next_digit := find_next_digit(line, offset=last_digit_result.end):
        last_digit_result = next_digit
    return first_digit_result.digit, last_digit_result.digit


def digits_to_number(digit1: str, digit2: str) -> int:
    return int(f"{digit1}{digit2}")


def compute_result(lines: Iterable) -> int:
    result = 0
    for line in lines:
        d1, d2 = find_first_and_last_digit(line)
        result += digits_to_number(d1, d2)
    return result


@click.command()
@click.argument("inputfile", type=click.File())
def cli(inputfile) -> None:
    print(compute_result(read_input(inputfile)))


if __name__ == "__main__":
    cli()
