

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
    test_case = ["A man, a plan, a canal: Panama",
                 "race a car", "0P", "a", " "]
    solution = Solution()

    for s in test_case:
        print(solution.isPalindrome(s))
