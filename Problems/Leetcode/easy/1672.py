"""
https://leetcode.com/problems/richest-customer-wealth/description/
"""

from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # the_rich = 0
        # wealths = []
        # accounts_len = len(accounts)
        # for i in range(accounts_len):
        #     for j in accounts[i]:
        #         the_rich = the_rich + j
        #     wealths.append(the_rich)
        #     the_rich = 0
        # return max(wealths)

        # wealths = []
        # for wealth in accounts:
        #     wealths.append(sum(wealth))
        # return max(wealths)

        max_wealths = 0
        for wealth in accounts:
            aa = sum(wealth)
            max_wealths = max(max_wealths, aa)
        return max_wealths
