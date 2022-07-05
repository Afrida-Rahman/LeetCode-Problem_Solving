from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    return sorted([i * i for i in nums])


print(sortedSquares([-4, -1, 0, 3, 10]))
