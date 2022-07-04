from typing import List


def moveZeroes(nums: List[int]) -> None:
    a = []
    b = []
    for i in nums:
        if i != 0:
            a.append(i)
        else:
            b.append(i)
    nums.clear()
    nums.extend(a)
    nums.extend(b)
    print(nums)


print(moveZeroes([0, 1, 0, 3, 12]))
