# <입력>
"""
첫째 줄: 떡의 개수 N( 1 ≤ N ≤ 1,000,000 )와 요청한 떡의 총 길이 M( 1 ≤ N ≤ 2,000,000,000 )
둘째 줄: 떡의 개별 길이
"""

# <출력>
"""
M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 최댓값
"""

from sys import stdin
from typing import List
input = stdin.readline


# 파라메트릭 탐색
def solution1(nm: List[int] = None, arr: List[int] = None) -> None:
    _, m = nm if nm else map(int, input().rstrip().split())
    arr = sorted(arr) if arr else sorted(list(
        map(int, input().rstrip().split())))

    res = 0
    start = 1
    end = max(arr)

    while start <= end:
        total = 0
        mid = (start + end) // 2

        for v in arr:
            if v > mid:
                total += v - mid

        if total < m:
            end = mid - 1
        else:
            res = mid
            start = mid + 1

    print(res)


# 반복 횟수 비교를 위해 남겨놓음
# solution1 반복 횟수: [case1, case2] = [16, 28]
# solution2 반복 횟수: [case1, case2] = [40, 56]
# 파라메트릭 탐색 시 약 2배 이상 반복 비용 감소
def solution2(nm: List[int] = None, arr: List[int] = None) -> None:
    _, M = nm if nm else map(int, input().rstrip().split())
    arr = sorted(arr) if arr else sorted(list(
        map(int, input().rstrip().split())))

    res = 0
    for h in range(M, max(arr) + 1):
        total = 0

        for v in arr:
            if v > h:
                total += v - h

        if total == M:
            res = h
            break

        if total < M:
            res = h - 1
            break

    print(res)


if __name__ == "__main__":
    cases = [
        [[4, 6], [19, 15, 10, 17]],
        [[1, 3], [12, 9, 4, 5, 1, 3, 10]]
    ]
    outputs = [15, 9]
    for case, output in zip(cases, outputs):
        nm,  arr = case
        solution2(nm, arr)
