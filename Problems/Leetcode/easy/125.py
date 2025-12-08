"""
125. Valid Palindrome
Easy
Topics
Companies
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1) remove non alphanumeric characters and numbers from s
        # 2) then loop and use two point for check left side and right side characters are same
        # 3) if any dont matchs return false
        s = "".join(filter(str.isalnum, str(s))).lower()
        left = 0
        right = len(s) - 1

        while left < right:
            # check is left index value == right inde value
            if s[left] != s[right]:
                return False
            # increase & decrease
            left += 1
            right -= 1

        return True

        # 2nd way
        # return s[::-1] == s


s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))
