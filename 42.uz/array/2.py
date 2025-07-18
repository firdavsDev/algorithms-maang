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


def reverse(data, left: int, right: int) -> list:

    while left < right:
        data[left], data[right] = data[right], data[left]
        left += 1
        right -= 1


def rotate(nums: list, k: int) -> list:
    # Slice
    # last_nums = nums[-k:]
    # first_nums = nums[:-k]
    # return last_nums + first_nums
    k = k % len(nums)
    # reverse
    reverse(nums, 0, len(nums) - 1)  # 0, 3
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)  # 5, 3
    return nums


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    k = 5

    result = rotate(nums, k)
    print(result)
