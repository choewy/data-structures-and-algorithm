# https://leetcode.com/problems/longest-palindrome/


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counters = {c: s.count(c) for c in s}

        is_exist_odd = 0
        for character, count in counters.items():
            if count % 2 == 1:
                counters[character] = count - 1
                is_exist_odd = 1

        return sum(list(counters.values())) + is_exist_odd
