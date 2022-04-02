from sys import stdin

input = stdin.readline


def solution() -> None:
    for num in sorted([int(input()) for _ in range(int(input()))]):
        print(num)


solution()
