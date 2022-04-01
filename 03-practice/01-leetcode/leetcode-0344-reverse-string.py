from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]

        # 확인용
        # print(s)


if __name__ == "__main__":
    test_case = [
        ["h", "e", "l", "l", "o"],
        ["H", "a", "n", "n", "a", "h"]
    ]
    solution = Solution()

    for s in test_case:
        solution.reverseString(s)
