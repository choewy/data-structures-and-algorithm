# https://leetcode.com/problems/group-anagrams/


from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 문자열의 문자를 정렬하여 key로 하고
        # 빈 리스트를 value로 하는 딕셔너리 생성
        words = {''.join(sorted(word)): [] for word in strs}

        # 입력받은 문자열 리스트를 반복하면서
        # 문자를 정렬하여 key로 하여 접근하고
        # 딕셔너리의 리스트에 문자열을 추가
        for word in strs:
            words[''.join(sorted(word))].append(word)

        # 딕셔너리의 value만 리스트로 변환하여 반환
        return list(words.values())
