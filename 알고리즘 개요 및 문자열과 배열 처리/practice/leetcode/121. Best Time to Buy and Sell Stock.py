from pprint import pprint
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices.pop(0)
        profit = 0

        while prices:
            price = prices.pop(0)

            if price < buy:
                buy = price

            if profit < price - buy:
                profit = price - buy

        return profit


# 테스트
if __name__ == "__main__":
    test_case = [
        {
            "input": [3, 2, 6, 5, 0, 3],
            "expected": 4
        },
        {
            "input": [2, 4, 1],
            "expected": 2
        },
        {
            "input": [2, 1, 4],
            "expected": 3
        },
        {
            "input": [7, 1, 5, 3, 6, 4],
            "expected": 5
        },
        {
            "input": [7, 6, 4, 3, 1],
            "expected": 0
        },
    ]

    def testing():
        solution = Solution()
        for case in test_case:
            i = case["input"]
            o = solution.maxProfit(i)
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
