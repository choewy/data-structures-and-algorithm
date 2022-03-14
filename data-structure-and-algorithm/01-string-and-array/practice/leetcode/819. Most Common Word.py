from pprint import pprint
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = list(paragraph)
        for i, c in enumerate(paragraph):
            paragraph[i] = c.lower() if c.isalpha() else ' '

        output = {}
        words = ''.join(paragraph).split()
        for word in words:
            if word not in banned:
                output[word] = output[word] + 1 if word in output.keys() else 1

        return sorted(output.items(), key=lambda x: -x[1])[0][0]


if __name__ == "__main__":
    test_case = [
        {
            "input": ["a, a, a, a, b,b,b,c, c", ["a"]],
            "expected": "b"
        },
        {
            "input": ["Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]],
            "expected": "ball"
        },
        {
            "input": ["a.", []],
            "expected": "a"
        },
        {
            "input": ["Bob. hIt, baLl", ["bob", "hit"]],
            "expected": "ball"
        }
    ]

    def testing():
        solution = Solution()
        for case in test_case:
            i = case["input"]
            o = solution.mostCommonWord(i[0], i[1])
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
