from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # v1 - Bad solution (On**2)
        # for i in range(len(nums) + 1):
        #     for j in range(i + 1, len(nums)):
        #         if target == nums[i] + nums[j]:
        #             print([i, j])
        # return None

        # v2 using enumrate
        listLenth = len(nums)
        for i in range(listLenth):
            if target == nums[i] + nums[i + 1]:
                print([i, i + 1])


if __name__ == "__main__":
    Solution().twoSum([3, 2, 3], 6)  # [0, 2]
