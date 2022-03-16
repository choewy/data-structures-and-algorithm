# 제출
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashtable = {jewel: stones.count(jewel)
                     for jewel in set(jewels)}

        return sum(hashtable.values())


# 테스트
if __name__ == "__main__":
    solution = Solution()
    print(solution.numJewelsInStones('aA', 'aAAbbbb'))
