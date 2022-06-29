from typing import List


def findNumbers(nums: List[int]) -> int:
    c = 0
    for i in nums:
        if len(str(i)) % 2 == 0:
            c += 1

    return c


print(findNumbers([555, 901, 482, 1771]))
