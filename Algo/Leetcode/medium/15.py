"""
https://leetcode.com/problems/3sum/

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.


Hint:
1. Birinchi qadam: Arrayni sort qiling

Nima uchun? Chunki takrorlanuvchi javoblarni osonroq boshqarish mumkin
Misol: [-1,0,1,2,-1,-4] → [-4,-1,-1,0,1,2]

2. Asosiy g'oya:

Birinchi raqamni tanlab oling (masalan nums[i])
Qolgan ikki raqamni Two Sum kabi topishga harakat qiling
Ya'ni: nums[j] + nums[k] = -nums[i] bo'ladigan j va k ni toping

3. Takrorlanuvchi javoblarni oldini olish:

Bir xil raqamlarni o'tkazib yuborishingiz kerak ba'zi joylarda

Bu yetarli hint. Endi o'zingiz sinab ko'ring!

"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        nums_len = len(nums)
        lst = []

        for i in range(nums_len):
            # Tashqi loop uchun duplicate skip
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            f_value = nums[i]
            left = i + 1
            right = nums_len - 1

            while left < right:
                sum_value = nums[left] + nums[right]

                if sum_value == -f_value:
                    lst.append([f_value, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Ichki loop uchun duplicate skip
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif sum_value > -f_value:
                    right -= 1
                elif sum_value < -f_value:
                    left += 1

        return lst


if __name__ == "__main__":
    # nums = [-1, 0, 1, 2, -1, -4]
    # nums = [0, 0, 0, 0]
    nums = [1, -1, -1, 0]
    obj = Solution()
    result = obj.threeSum(nums=nums)
    print(result)
