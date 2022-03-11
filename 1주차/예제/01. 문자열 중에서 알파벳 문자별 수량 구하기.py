# 문자열 중에서 알파벳 문자별 수량 구하기

from string import ascii_lowercase
from pprint import pprint


# 나쁜 풀이
def bad(string: str) -> None:
    characters = {}

    # ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"
    for lowercase in ascii_lowercase:
        for character in string:
            if character == lowercase:
                if lowercase not in characters.keys():
                    characters[lowercase] = 1
                    continue
                characters[lowercase] += 1

    pprint(characters)


# 풀이 개선
def better(string: str) -> None:
    characters = {}

    for character in string:
        if character in ascii_lowercase:
            if character not in characters.keys():
                characters[character] = 1
                continue
            characters[character] += 1

    pprint(characters)


# 좋은 풀이
def good(string: str) -> None:
    characters = {}

    for character in string:
        if not character.isalpha():
            continue
        if character not in characters.keys():
            characters[character] = 1
            continue
        characters[character] += 1

    pprint(characters)


if __name__ == "__main__":
    string = "hello my name is hanghea99"
