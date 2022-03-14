# 배열 내 특정 숫자의 존재 여부 파악하기

from pprint import pprint

numbers = [3, 5, 6, 1, 2, 4]


def bad(number: int) -> None:
    for element in numbers:
        if element == number:
            return print(True)

    print(number)


def good(number: int) -> None:
    print(number in numbers)


if __name__ == "__main__":
    number = 5
