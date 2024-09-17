"""
#easy #algorithms

Find 2 number sum is equal to target:

"""

numbers = [1, 5, 4, 2, 6, 7, 9, 3]
target = 3


# 1 varyant  O(n^2)
def two_number_sum_v1(numbers: list, target) -> list:
    """
    Use nested loops
    """
    for i in numbers:
        for j in numbers:
            if i + j == target:
                return [i, j]
    return []


"""
Big O darajasi:
- bu yerda biz listdagi barcha element'larni birma bir loop qilib yurib chiqyapmiz O(n)
- listda qancha item bulishi mumkin bu bizga noma'lum va biz buni n deb ataymiz va O(n) marta ish bajargan bulamiz
- va 2ta nested(ichma ich) loop(aylanish) bo'lgani sababli biz O(n^2) ish qilgan bulamiz.
Xotiradan deyarli foydalanilmadi: O(1)
"""

print(two_number_sum_v1(numbers=numbers, target=target))

######################################################### V2 #########################################################


def two_number_sum_v2(numbers: list, target: int):
    """
    Use one loop
    Bizda:
        X va Y qo'shilganda target natija bo'ladi (x + y = target )
        Demak y =  (target - x)ga teng
    """
    nums = {}  # bu yerda biz raqamlarni yigib boramiz
    for X in numbers:
        # y = target - X(bu yerda array ichidagi raqam)
        Y = target - X
        if Y in nums:
            return [Y, X]
        else:
            nums[X] = True  # agar topilmasa uni topilmagan raqamlar ichiga qushamiz
    return []


# O(n) vaqt
# O(n) xotira
# chunki biz array'ni bir marta aylandik va hotiradan arrayda nechta item bulsa shuncha item qushib bordik (dict'ga)
print(two_number_sum_v2(numbers, target))


######################################################### V3 #########################################################


def two_number_sum_v3(numbers: list, target: int):
    """
    Use pointers after sort item in array:
    ! .sort() orqali tartiblab olamiz

    x = [1,4,5, ... 8, 4]
         ^             ^
         |             |
      Left point(x),  Right point(y)

    Agar x + y < target bo'lsa biz left point bir qadam oldinga surib kelamiz
    Agar x + y > target bo'lsa biz right point bir qadam orqaga surib boramiz
    Agar x + y = target bo'lsa natijani qaytaramiz!
    """
    # tartiblaymiz
    numbers.sort()

    # left va right point'lar (indexlar)
    left_point = 0
    right_point = len(numbers) - 1

    # left point'imizda right point'imiz o'tib ketmasligi kerak
    # shu bois left < right bo'lishiga qadar jarayoni bajaramiz
    while left_point < right_point:
        # X + Y
        X = numbers[left_point]
        Y = numbers[right_point]
        X_plus_Y = X + Y

        # X + Y = target
        if X_plus_Y == target:
            return [X, Y]
        elif X_plus_Y < target:
            # chap pointni 1 ta qadamga oldinga suramiz
            left_point += 1
        elif X_plus_Y > target:
            # right point ni 1taga kamaytiramiz
            right_point -= 1

    return []


# O(nLog(n)) time
# O(1) xotira (hech qanday data saqlamadim data structure qilib)
print(two_number_sum_v3(numbers, target))
