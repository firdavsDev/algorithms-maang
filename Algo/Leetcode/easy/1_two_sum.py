from typing import List


def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    numsLenth = len(nums)
    for index_i, value_i in enumerate(nums):
        for index_j, value_j in enumerate(nums, index_i + 1):
            print(value_j)
            if target == value_i + value_j:
                return [index_i, index_j]
    return []


nums = [-5, -2, 3, 4, 6]
# nums = [1, 1, 1]
target = 7
print(pair_sum_sorted(nums=nums, target=target))

# O(n**2)
