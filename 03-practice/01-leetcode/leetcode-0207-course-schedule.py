# https://leetcode.com/problems/course-schedule/

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    solution = Solution()
    print(solution.canFinish(2, [[1, 0]]) == True)
    print(solution.canFinish(2, [[1, 0], [0, 1]]) == False)
