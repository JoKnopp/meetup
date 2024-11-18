#!/usr/bin/env python3
from typing import Iterator, Iterable, NamedTuple

import click
import re


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


def find_next_digit_gpt4(text: str, offset: int = 0) -> int:
    # Define a dictionary to map written words to their corresponding digits
    word_to_digit = {
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

    # Define regex patterns for digits (1-9) and written numbers without word boundaries
    digit_pattern = re.compile(r"[1-9]")
    word_pattern = re.compile(r"one|two|three|four|five|six|seven|eight|nine")

    # Exclude portion of text before the offset for matching
    searchable_text = text[offset:]

    # Search for the first occurrence of a digit
    digit_match = digit_pattern.search(searchable_text)

    # Search for the first occurrence of a written number
    word_match = word_pattern.search(searchable_text)

    # Find positions
    digit_index = digit_match.start() + offset if digit_match else float("inf")
    word_index = word_match.start() + offset if word_match else float("inf")

    # Determine which is found first
    if digit_index < word_index:
        return DigitSearchResult(
            digit=digit_match.group(), start=digit_index, end=digit_match.end() + offset
        )
    elif word_index < digit_index:
        word = word_match.group()
        return DigitSearchResult(
            digit=word_to_digit[word], start=word_index, end=word_match.end() + offset
        )
    else:
        return None  # No occurrence found


def find_first_and_last_digit(line: str) -> tuple[int, int]:
    first_digit_result: DigitSearchResult = find_next_digit_gpt4(line)
    if first_digit_result is None:
        raise ValueError(f"At least one digit expected on each line. Found none for {line=}")
    last_digit_result = first_digit_result
    while next_digit := find_next_digit_gpt4(line, offset=last_digit_result.start + 1):
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
