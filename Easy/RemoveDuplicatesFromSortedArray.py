from typing import List


def removeDuplicates(nums: List[int]) -> int:
    a = set(nums)
    nums.clear()
    nums.extend(a)
    nums.sort(reverse=False)
    return len(list(nums))


print(removeDuplicates([-1, 0, 0, 0, 0, 3, 3]))
