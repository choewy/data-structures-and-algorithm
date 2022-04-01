from pprint import pprint
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)
        stack = []

        for i, temperature in enumerate(temperatures):
            while stack:
                if temperatures[stack[-1]] >= temperature:
                    break
                index = stack.pop()
                output[index] = i - index
            stack.append(i)

        return output


if __name__ == "__main__":
    test_case = [
        {"input": [34, 80, 80, 80, 34, 80, 80, 80, 34, 34],
            "expected": [1, 0, 0, 0, 1, 0, 0, 0, 0, 0]},
        {"input": [73, 74, 75, 71, 69, 72, 76, 73],
            "expected": [1, 1, 4, 2, 1, 1, 0, 0]},
        {"input": [30, 40, 50, 60], "expected": [1, 1, 1, 0]},
        {"input": [30, 60, 90], "expected": [1, 1, 0]},
    ]

    def test():
        for case in test_case:
            i = case["input"]
            e = case["expected"]
            o = solution.dailyTemperatures(i)

            if o != e:
                case["result"] = False
                case["output"] = o
                return pprint(case)

        print(True)

    solution = Solution()
    test()
