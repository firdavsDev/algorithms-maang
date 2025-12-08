# 217. Contains Duplicate https://leetcode.com/problems/contains-duplicate/description/
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(nums) != len(set(nums))
        # bad version (Space )
        dubNum = set()
        for num in nums:
            if num in dubNum:
                return True
