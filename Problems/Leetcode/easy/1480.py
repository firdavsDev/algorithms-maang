#
# @lc app=leetcode id=1480 lang=python
#
# [1480] Running Sum of 1d Array
#


# @lc code=start
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # bad version
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                print(f"{i} - {j}")


# @lc code=end
