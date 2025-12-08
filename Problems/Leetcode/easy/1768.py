"""
1768. Merge Strings Alternately
Easy

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.


Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len = len(word1)
        word2_len = len(word2)
        new_list = []
        glob_word_2_index = 0

        for word_1_index in range(word1_len):
            for word_2_index in range(word2_len):
                new_list.append(f"{word1[word_1_index]}{word2[glob_word_2_index]}")
                glob_word_2_index += 1
                break
            if word1_len > word2_len:
                new_list.extend(word1[:word_1_index])
            if word1_len < word2_len:
                new_list.extend(word2[:word_2_index])
        return "".join(new_list)


word1 = "abcd"
word2 = "pq"
print(Solution().mergeAlternately(word1, word2))
