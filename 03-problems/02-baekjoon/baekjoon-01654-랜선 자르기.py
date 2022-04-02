from typing import List
from sys import stdin

input = stdin.readline


def solution(kn: List[int] = None, arr: List[int] = None) -> None:
    k, n = kn if kn else map(int, input().rstrip().split())
    arr = arr if arr else [int(input().rstrip()) for _ in range(k)]

    _min = 1
    _max = max(arr)

    while _min <= _max:
        _mid = (_min + _max) // 2
        _sum = 0
        for v in arr:
            _sum += v // _mid

        if _sum < n:
            _max = _mid - 1
        else:
            _min = _mid + 1

    print(_max)


if __name__ == "__main__":
    cases = [
        [[4, 11], [802, 743, 457, 539]],
        [[2, 1], [20, 1]],
        [[5, 6], [1, 3, 5, 7, 9]],
    ]
    outputs = [200, 20, 3]

    for case, output in zip(cases, outputs):
        mn, arr = case
        solution(mn, arr)
