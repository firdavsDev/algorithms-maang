"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            sumValue = numbers[left] + numbers[right]
            if sumValue == target:
                return [left + 1, right + 1]
            elif sumValue > target:
                right -= 1
            elif sumValue < target:
                left += 1

data = [1,2,3,4,5,6,7,8,9,10], target=11