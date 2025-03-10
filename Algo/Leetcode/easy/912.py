# 912. Sort an Array
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Selection sort
        # size = len(nums)

        # for ind in range(size):
        #     min_index = ind

        #     for j in range(ind + 1, size):
        #         if nums[j] < nums[min_index]:
        #             min_index = j
        #     # swapping the elements to sort the array
        #     (nums[ind], nums[min_index]) = (nums[min_index], nums[ind])
        # return nums

        if len(nums) <= 1:
            return nums
        else:
            pivot = nums[0]
            left = [x for x in nums[1:] if x < pivot]
            right = [x for x in nums[1:] if x >= pivot]
            return self.sortArray(left) + [pivot] + self.sortArray(right)


nums = [5, 2, 3, 1]
s = Solution().sortArray(nums)
print(s)
# Output: [1,2,3,5]
