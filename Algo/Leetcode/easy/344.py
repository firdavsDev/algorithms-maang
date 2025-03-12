"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.



Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            # swap
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        # qisqa loop
        # n = len(s)
        # for i in range(n // 2):
        #     s[i], s[n - 1 - i] = s[n - 1 - i], s[i]


s = ["H", "a", "n", "n", "a", "h"]
excepted = ["h", "a", "n", "n", "a", "H"]
Solution().reverseString(s)
print(s == excepted)
