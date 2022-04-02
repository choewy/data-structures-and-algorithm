class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for c in s:
            if c.isalpha():
                chars.append(c.lower())
            elif c.isdigit():
                chars.append(c)

        while len(chars) > 1:
            if chars.pop(0) != chars.pop():
                return False

        return True


if __name__ == "__main__":
    cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " ",
    ]
    outputs = [True, False, True]

    solution = Solution()
    for case, output in zip(cases, outputs):
        print(solution.isPalindrome(case) == output)
