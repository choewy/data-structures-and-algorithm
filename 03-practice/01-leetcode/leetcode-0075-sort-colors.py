# <문제>
"""
내장 라이브러리를 사용하지 말고,
주어진 배열을 오름차순으로 정렬하라.
단, 값은 반환하지 않고 배열 내부 순서를 변경하라.
"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # 반칙 쓰면? (34 ms, 13.8 MB)
        nums.sort()


if __name__ == "__main__":
    cases = [
        [2, 0, 2, 1, 1, 0],
        [2, 0, 1]
    ]

    outputs = [
        [0, 0, 1, 1, 2, 2],
        [0, 1, 2]
    ]

    solution = Solution()

    for case, output in zip(cases, outputs):
        solution.sortColors(case)
        print(case == output)
