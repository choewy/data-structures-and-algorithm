from pprint import pprint
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == "__main__":
    test_case = [
        {
            "input": [[2, 7, 11, 15], 9],
            "expected": [0, 1]
        },
        {
            "input": [[3, 2, 4], 6],
            "expected": [1, 2]
        },
        {
            "input": [[3, 3], 6],
            "expected": [0, 1]
        }
    ]

    def testing():
        solution = Solution()
        for case in test_case:
            i = case["input"]
            o = solution.twoSum(i[0], i[1])
            e = case["expected"]
            if o != e:
                return {
                    "result": False,
                    "input": i,
                    "output": o,
                    "expected": e
                }

        return {"result": True}

    pprint(testing())
