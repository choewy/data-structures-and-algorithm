from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            for j in range(len(res)):
                res.append(res[j] + [n])
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.subsets([1, 2, 3]) == [
        [], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]
    ])
    print(solution.subsets([0]) == [[], [0]])
