"""
https://leetcode.com/problems/fizz-buzz/
"""

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # lst = []
        # for i in range(1,n+1):
        #     if i % 3 == 0 and i % 5 == 0:
        #         lst.append("FizzBuzz")
        #     elif i % 3 == 0:
        #         lst.append("Fizz")
        #     elif i % 5 == 0:
        #         lst.append("Buzz")
        #     else:
        #         lst.append(str(i))
        # return lst

        # return [
        #     "FizzBuzz" if i % 3 == 0 and i % 5 == 0
        #     else "Fizz" if i % 3 == 0
        #     else "Buzz" if i % 5 == 0
        #     else str(i)
        #     for i in range(1, n + 1)
        # ]

        lst = []
        for i in range(1, n + 1):

            text = ""
            if i % 3 == 0:
                text += "Fizz"

            if i % 5 == 0:
                text += "Buzz"

            if len(text) == 0:
                text += str(i)

            lst.append(text)

        return lst
