"""
189. Rotate Array
Medium
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.



Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # bad version
        # for _ in range(k):
        #     num = nums.pop()
        #     nums.insert(0, num)
        # v2
        # nums_len = len(nums) - 3
        # print(nums[-k:] + nums[:nums_len])


if __name__ == "__main__":
    nums, k = [1, 2, 3, 4, 5, 6, 7], 3
    Solution().rotate(nums=nums, k=k)
    print(nums)
