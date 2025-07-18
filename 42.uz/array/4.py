"""
Ro'yxat kvadrati
Sizga berilgan sonlar ro'yxati o'sish tartibida saralangan. Har bir elementning kvadratini hisoblab, natijani saralangan holda qaytaring.

Misol 1:
Kiritish: nums = [-4,-1,0,3,10]
Natija: [0,1,9,16,100]
Misol 2:
Kiritish: nums = [-7,-3,2,3,11]
Natija: [4,9,9,49,121]
"""


def custom_reverse(data: list) -> list:
    left, right = 0, len(nums) - 1

    while left < right:
        data[left], data[right] = data[right], data[left]
        left += 1
        right -= 1
    return data


def sortedSquares(nums: list) -> list:
    lst = []
    # for num in nums:
    #     lst.append(num**2)
    # return sorted(lst)
    left, right = 0, len(nums) - 1

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            lst.append(nums[left] ** 2)
            left += 1
        else:
            lst.append(nums[right] ** 2)
            right -= 1

    return custom_reverse(lst)


if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]
    res = sortedSquares(nums)
    print(res)  # [0, 1, 9, 16, 100]
