from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for ind, num in enumerate(nums):
            if target - num in a:
                return [a[target - num], ind]

            else:
                a[num] = ind