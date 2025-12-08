"""
680. Valid Palindrome II
Easy
Topics
Companies
Given a string s, return true if the s can be palindrome after deleting at most one character from it.


Example 1:

Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
"""


class Solution:

    def is_palindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def validPalindrome(self, s: str) -> bool:

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # Chap yoki o‘ng harfni olib tashlab tekshiramiz
                return self.is_palindrome(s, left + 1, right) or self.is_palindrome(
                    s, left, right - 1
                )
            left += 1
            right -= 1
        return True


s = "pidbliassaqozokmtgahluruufwbjdtayuhbxwoicviygilgzduudzgligyviciowxbhuyatdjbwfuurulhagtmkozoqassailbdip"  # false
print(Solution().validPalindrome(s))
