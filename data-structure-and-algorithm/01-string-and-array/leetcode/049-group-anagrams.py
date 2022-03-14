# https://leetcode.com/problems/group-anagrams/


from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {''.join(sorted(word)): [] for word in strs}

        for word in strs:
            words[''.join(sorted(word))].append(word)

        return list(words.values())
