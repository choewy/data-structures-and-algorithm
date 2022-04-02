from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x[0] for x in sorted({n: nums.count(n) for n in set(nums)}.items(), key=lambda x: (-x[1], x[0]))[:k]]


if __name__ == "__main__":
    solution = Solution()
    print(solution.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2))
