from pprint import pprint
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        hashtbl = {}
        for num in set(nums):
            if num not in hashtbl.keys():
                cnt = nums.count(num) - 1
                tmp = [str(n) for n in nums if n != num] + [str(num)]*cnt
                val = eval("*".join(tmp))
                hashtbl[num] = val

        return [hashtbl[num] for num in nums]


if __name__ == "__main__":
    test_case = [
        {
            "input": [-1, 1, 0, -3, 3],
            "expected": [0, 0, 9, 0, 0]
        },
        {
            "input": [1, 2, 3, 4],
            "expected": [24, 12, 8, 6]
        },
    ]

    def testing():
        solution = Solution()
        for case in test_case:
            i = case["input"]
            o = solution.productExceptSelf(i)
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
