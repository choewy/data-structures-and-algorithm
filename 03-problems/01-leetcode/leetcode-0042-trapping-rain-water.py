from pprint import pprint
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        max_h = max(height)
        water = 0

        for _ in range(max_h):
            floor = []
            start, end = None, 0
            for i, h in enumerate(height):
                if h > 0:
                    height[i] -= 1
                    floor.append(1)
                    if start is None:
                        start = i
                    end = i
                else:
                    floor.append(0)
            water += floor[start:end+1].count(0)

        return water


if __name__ == "__main__":
    test_case = [
        {
            "input": [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
            "expected": 6
        },
        {
            "input": [4, 2, 0, 3, 2, 5],
            "expected": 9
        }
    ]

    def testing():
        solution = Solution()
        for case in test_case:
            i = case["input"]
            o = solution.trap(i)
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
