# <문제>
"""
첫째 줄 : 나무의 수 N(1 ≤ N ≤ 1,000,000)과 나무의 길이 M(1 ≤ M ≤ 2,000,000,000)
둘째 줄 : 나무의 높이 H(0 ≤ H ≤1,000,000,000)
"""


from typing import List


def solution(nm: List[int] = None, arr: List[int] = None) -> None:
    _, m = nm if nm else map(int, input().rstrip().split())
    arr = sorted(arr) if arr else sorted(list(
        map(int, input().rstrip().split())))

    res = 0
    start = 1
    end = max(arr)

    while start <= end:
        mid = (start + end) // 2
        total = 0

        for v in arr:
            if v > mid:
                total += v - mid

        if total < m:
            end = mid - 1
        else:
            res = mid
            start = mid + 1

    print(res)


if __name__ == "__main__":
    cases = [
        [[4, 7], [20, 15, 10, 17]],
        [[5, 20], [4, 42, 40, 26, 46]],
        [[4, 2], [1, 1, 0, 0, 0]],
        [[6, 3], [1, 1, 4, 5, 3, 6]]
    ]
    outputs = [15, 36, 0, 3]
    for case, output in zip(cases, outputs):
        nm,  arr = case
        solution(nm, arr)
