# <문제>
"""
N개의 2차원 좌표를 다음 우선순위에 따라 정렬하라.
1) y좌표를 기준으로 오름차순 정렬
2) x좌표를 기준으로 오름차순 정렬
"""

# <입력>
"""
1) Line 1 : 점의 개수 N
2) Line 2 ~ (N + 1) : x와 y좌표 값
"""


# <제출>
from typing import List
from sys import stdin
input = stdin.readline


def solution(N: int = None, grid: List[iter] = None) -> None:
    N = N if N else int(input().rstrip())
    grid = grid if grid else [
        tuple(map(int, input().rstrip().split())) for _ in range(N)]
    grid = sorted(grid, key=lambda xy: (xy[1], xy[0]))

    for (x, y) in grid:
        print(f"{x} {y}")


if __name__ == "__main__":
    testcases = [
        [5, [(0, 4), (1, 2), (1, -1), (2, 2), (3, 3)]]
    ]

    for case in testcases:
        N, grid = case
        solution(N, grid)
