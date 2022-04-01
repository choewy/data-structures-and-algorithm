class Solution:
    def check(self, i, s):
        l = [s[i]]
        for c in s[i+1:]:
            if c not in l:
                l.append(c)
            else:
                return l

        return l

    def lengthOfLongestSubstring(self, s: str) -> int:
        lens = [0]

        for i in range(len(s)):
            word = self.check(i, s)
            lens.append(len(word))

        return max(lens)


if __name__ == "__main__":
    solution = Solution()
    solution.lengthOfLongestSubstring('pwwkew')
