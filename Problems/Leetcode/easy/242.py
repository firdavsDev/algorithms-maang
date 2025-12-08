# 242. Valid Anagram https://leetcode.com/problems/valid-anagram/description/

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
