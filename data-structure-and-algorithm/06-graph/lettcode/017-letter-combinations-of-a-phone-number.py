from typing import List


dials = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
         "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}


class Solution1:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        def recursive(index, path) -> None:
            if len(path) == len(digits):
                return res.append(path)

            for i in range(index, len(digits)):
                for c in dials[digits[i]]:
                    recursive(i+1, f'{path}{c}')

        res = []
        recursive(0, "")
        return res


class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        if len(digits) == 1:
            return dials[digits]

        def makeCombinatinos(current: List[str], next: List[str]) -> List[str]:
            return [cc + nc for nc in next for cc in current]

        chars = [dials[digit] for digit in digits]
        res = list(chars[0])

        for char in chars[1:]:
            res = makeCombinatinos(res, char)

        return res


if __name__ == "__main__":
    solution = Solution2()
    print(solution.letterCombinations('234'))
