"""
Berilgan ro'yxatni k qadam o'ng tomonga aylantiring.

Ro'yxatni 1 qadam o'ng tomonga aylantirish, o'ng tomondagi ohirgi elementni, chap tomonning boshiga olib qo'yish degani.

Amalni berilgan ro'yhat ustida bajaring - yangi ro'yxat yaratmang.

Misol 1:
Kiritish: nums = [1,2,3,4,5,6,7], k = 3
Natija: [5,6,7,1,2,3,4]
Tushuntirish:
1-qadam: [7,1,2,3,4,5,6]
2-qadam: [6,7,1,2,3,4,5]
3-qadam: [5,6,7,1,2,3,4]
"""


def rotate(nums: list, k: int) -> list:

    for i in range(k):
        nums[0] = nums[-i]
        print(nums)
    return nums


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    result = rotate(nums, k)
    print(result)
