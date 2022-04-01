from typing import List


class Solution:
    def recursive(self, nums: List[int], path: List[int], res: List[int]):
        if not nums:
            res.append(path)

        for i in range(len(nums)):
            np = path + [nums[i]]
            ns = nums[:i] + nums[i+1:]
            self.recursive(ns, np, res)

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        res = []
        self.recursive(nums, [], res)

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.permute([5, 4, 6, 2]))
