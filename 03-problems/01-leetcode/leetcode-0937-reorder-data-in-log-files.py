from typing import List
from pprint import pprint


class Solution:
    def value_type_check(self, s):
        for c in s:
            if c.isdigit():
                return 0
            return 1

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 조건
        #   1) digit 보다 letter가 먼저 위치하여야 한다.
        #   2) letter는 key, 값 순으로 정렬되어야 한다.

        letters = []
        digits = []

        for log in logs:
            temp = log.split(" ")
            value = ' '.join(temp[1:])
            type_check = self.value_type_check(value)
            letters.append([temp[0], value]) if type_check else digits.append(
                [temp[0], value])

        letters = sorted(letters, key=lambda x: x[0])
        letters = sorted(letters, key=lambda x: x[1])
        return [' '.join(log) for log in letters + digits]


if __name__ == "__main__":
    test_case = [{
        "input": ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"],
        "expected": ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
    }, {
        "input": ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"],
        "expected": ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]
    }]

    def testing():
        solution = Solution()
        for case in test_case:
            i = case["input"]
            o = solution.reorderLogFiles(i)
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
