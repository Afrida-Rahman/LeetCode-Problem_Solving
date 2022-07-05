from typing import List


def removeElement(nums: List[int], val: int) -> int:
    a = []
    for i in range(len(nums)):
        if nums[i] != val:
            a.append(nums[i])
    nums.clear()
    nums.extend(a)
    return len(a)


print(removeElement([3, 2, 2, 3], 3))
