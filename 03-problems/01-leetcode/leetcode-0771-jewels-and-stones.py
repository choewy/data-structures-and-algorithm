# 제출
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum({jewel: stones.count(jewel) for jewel in set(jewels)}.values())


# 테스트
if __name__ == "__main__":
    solution = Solution()
    print(solution.numJewelsInStones('aA', 'aAAbbbb'))
