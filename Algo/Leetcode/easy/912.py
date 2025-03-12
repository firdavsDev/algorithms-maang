# 912. Sort an Array
"""
Quic sort:

stack holatda rekursiya funksiyalarni qabul qila oladi va TASODIFAN pivot raqam tanlanganda (Onlogn) sifat buladi

"""

from random import randrange
from typing import List


def partition(self, nums, low, high):
    # Tasodifiy pivot tanlaymiz va uni oxirga swap qilamiz
    pivot_idx = randrange(low, high + 1)
    nums[pivot_idx], nums[high] = nums[high], nums[pivot_idx]
    pivot = nums[high]

    i = low - 1  # Kichik elementlar uchun ko'rsatkich
    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1


class Solution:
    def __init__(self):
        self.n = 1

    def qsortInPlace(self, nums, low, high):
        print(f"{self.n}) qsortInPlace: nums={nums}, low={low}, high={high}")
        self.n = self.n + 1

        if low < high:  # base case (tuhtash nuqtasi)
            pivot_idx = partition(nums, low, high)
            self.qsortInPlace(nums, low, pivot_idx - 1)
            self.qsortInPlace(nums, pivot_idx + 1, high)
        return nums

    def qsort(self, nums):
        """Quicksort

        Args:
            nums (list): numbers

        Returns:
            list: array of numbers
        """
        size = len(nums)
        if size < 2:
            return nums
        else:
            pivot = nums.pop(randrange(size))
            left = [x for x in nums if x <= pivot]
            right = [x for x in nums if x > pivot]
            return self.qsort(left) + [pivot] + self.qsort(right)

    def sSort(self, nums):
        """SelectionSort

        Args:
            nums (list): numbers list
        """
        size = len(nums)

        for ind in range(size):
            min_index = ind

            for j in range(ind + 1, size):
                if nums[j] < nums[min_index]:
                    min_index = j
            # swapping the elements to sort the array
            (nums[ind], nums[min_index]) = (nums[min_index], nums[ind])
        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        # Selection sort
        # print("Selection Sort", self.sSort(nums))
        # Quicksort
        # print("Quicksort", self.qsort(nums))
        print("qsortInPlace", self.qsortInPlace(nums=nums, low=0, high=len(nums) - 1))


nums = [5, 2, 3, 1]
print("Orginal array: ", nums)
Solution().sortArray(nums)
print("After sorting orginal array", nums)

# Expected Output: [1,2,3,5]
