from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        items = {n: nums.count(n) for n in set(nums)}.items()
        items = sorted(hashitems, key=lambda x: (-x[1], x[0]))[:k]
        return [x[0] for x in items]


if __name__ == "__main__":
    solution = Solution()
    print(solution.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2))
