from pprint import pprint
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 반복문으로 해야함
        # 이유? 아래 테스트케이스 첫 번째와 같이
        # 사려는 값을 최소값으로 구하는 경우
        # 찾을 수 없는 상횡이 발생할 수 있음

        buy = min(prices)
        buy_index = prices.index(buy)

        prices = prices[buy_index:]
        sell = max(prices)
        sell_index = prices.index(sell) + buy_index

        if buy_index < sell_index:
            return sell - buy

        return 0


# 테스트
if __name__ == "__main__":
    test_case = [
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
