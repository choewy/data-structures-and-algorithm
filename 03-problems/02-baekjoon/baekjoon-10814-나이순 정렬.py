# <문제>

"""
회원들을 나이, 가입한 순서 순으로 정렬하라.
"""

from sys import stdin
input = stdin.readline


def solution() -> None:
    for member in sorted([(input().rstrip().split()+[n]) for n in range(int(input().rstrip()))], key=lambda x: (int(x[0]), x[2])):
        print(*member[:2])


if __name__ == "__main__":
    solution()
