"""169. Majority Element"

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
"""

from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dics = Counter(nums)
        for dic in dics:
            if dics[dic] > len(nums) / 2:
                return dic


if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    result = Solution().majorityElement(nums=nums)
    print(result)
