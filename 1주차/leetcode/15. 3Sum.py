from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        results = []

        # left, right가 중첩되지 않도록 하기 위해서
        for i in range(len(nums) - 2):
            # 검사 중복 방지
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 간격을 좁혀가며 합 sum 계산
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                # 합이 음수이면 left를 +1만큼 이동
                if sum < 0:
                    left += 1

                # 합이 양수이면 right를 -1만큼 이동
                elif sum > 0:
                    right -= 1

                # 합이 0이면 groups에 추가 후 스킵 처리
                else:
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return results
