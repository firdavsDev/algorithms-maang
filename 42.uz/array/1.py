"""
Nollarni orqaga surish
Berilgan sonlar ro'yxatidagi nollarni ro'yxat orqasiga o'tkazing, lekin boshqa elementlar ketma-ketligi buzilmasin.

Imkon qadar kamroq amal bajaring.

Qo'shimcha xotiradan foydalanmang - amallarni ro'yxat ustida bajaring.

Misol 1:
Kiritish: nums = [0,1,0,3,12]
Natija: [1, 3, 12, 0, 0]
"""


def moveZeroes(nums: list) -> list:
    # lenth = len(nums) - 1
    # for i in range(lenth):
    #     print("Lenth", lenth)
    #     if nums[i] == 0:
    #         zero = nums.pop(i)
    #         print(i, zero)
    #         print("after pop", nums)
    #         nums.insert(lenth, zero)
    #         print("after insert", nums)
    # return nums

    # count = nums.count(0)
    # for _ in range(count):
    #     nums.remove(0)
    #     nums.append(0)
    # return nums

    zero_count = 0
    for i, num in enumerate(nums):
        if num == 0:
            zero_count += 1
        else:
            nums[i], nums[i - zero_count] = nums[i - zero_count], nums[i]
    return nums


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]

    result = moveZeroes(nums)
    print(result)
