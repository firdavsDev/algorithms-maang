"""
- Nollarni orqaga surish
* Berilgan sonlar ro'yxatidagi nollarni ro'yxat orqasiga o'tkazing, lekin boshqa elementlar ketma-ketligi buzilmasin.
* Imkon qadar kamroq amal bajaring.
* Qo'shimcha xotiradan foydalanmang - amallarni ro'yxat ustida bajaring.

Misol 1:
Kiritish: nums = [0,1,0,3,12]
Natija: [1, 3, 12, 0, 0]
"""


def moveZeroes(nums: list) -> list:
    # version 1: O(n)
    # loop nums and check is 0 and remove and append new list
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
    return nums


nums = [0, 0, 0, 0, 1]
assert moveZeroes(nums) == [1, 0, 0, 0, 0], "Not true`"
