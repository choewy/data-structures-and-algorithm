# <문제>
"""
정수(양수)형 리스트가 주어지며,
이들을 문자열로 조합해서 가장 큰 수를 출력하라.
"""

from typing import List


# 모든 수를 검사하면서 직접 정렬
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(list(map(str, nums)), reverse=True)

        for i in range(1, len(nums)):
            ptr = i
            while ptr > 0:
                pre = nums[ptr - 1]
                cur = nums[ptr]
                x, y = pre + cur, cur + pre

                if x < y:
                    ptr = 0
                    continue

                nums[ptr - 1], nums[ptr] = nums[ptr], nums[ptr - 1]
                ptr -= 1

        return str(int(''.join(nums)))


# 과정 1
"""
nums: default = [3, 30, 34, 5, 9] 

i : 1 =>
        ptr : 1,
            pre = "3", cur: "30"
            x: "330", y: "303" => ptr: 0
        ptr : 0,
            End while
i : 2 =>
        ptr : 2, 
            pre: "30", cur: "34"
            x: "3034", y: "3430" => swap ["3", "34", "30", "5", "9"]
        ptr : 1, 
            pre: "3", cur: "34"
            x: "334", y: "343" => swap ["34", "3", "30", "5", "9"]
        ptr : 0,
            End while
i : 3 =>
        ptr : 3, 
            pre: "30", cur: "5"
            x: "305", y: "530" => swap ["34", "3", "5", "30", "9"]
        ptr : 2, 
            pre: "3", cur: "5"
            x: "35", y: "53" => swap ["34", "5", "3", "30", "9"]
        ptr : 1, 
            pre: "34", cur: "5"
            x: "345", y: "534" => swap ["5", "34", "3", "30", "9"]
        ptr : 0,
            End while
i : 4 =>
        ptr : 4, 
            pre: "30", cur: "9"
            x: "309", y: "903" => swap ["5", "34", "3", "9", "30"]
        ptr : 3, 
            pre: "3", cur: "9"
            x: "39", y: "93" => swap ["5", "34", "9", "3", "30"]
        ptr : 2, 
            pre: "34", cur: "9"
            x: "349", y: "934" => swap ["5", "9", "34", "3", "30"]
        ptr : 1, 
            pre: "5", cur: "9"
            x: "59", y: "95" => swap ["9", "5", "34", "3", "30"]
        ptr : 0,
            End while   
"""

# 과정 2(초벌 정렬)
"""
nums: sorted = ["9", "5", "34", "30", "3"]

i : 1 => 
        ptr : 1,
            pre: "9", cur: "5"
            x: "95", y: "59" => ptr: 0
        ptr : 0,
            End while
i : 2 =>
        ptr : 2,
            pre: "5", cur: "34"
            x: "534", y: "345" => ptr: 0
        ptr : 0,
            End while
i : 3 =>
        ptr : 3,
            pre: "34", cur: "30",
            x: "3430", y: "3034" => ptr: 0
        ptr : 0,
            End while
i : 4 =>
        ptr : 4,
            pre: "30", cur: "3",
            x: "303", y: "330" => swap ["9", "5", "34", "3", "30"]
        ptr : 3,
            pre: "34", cur: "3",
            x: "343", y: "334" => ptr: 0
        ptr : 0,
            End while
"""


if __name__ == "__main__":
    testcases = [[[10, 2], "210"], [[3, 30, 34, 5, 9], "9534330"]]

    solution = Solution()
    for case in testcases:
        nums, output = case
        print(solution.largestNumber(nums) == output)
