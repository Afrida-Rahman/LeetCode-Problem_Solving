from typing import List


def thirdMax(nums: List[int]) -> int:
    a = sorted(list(set(nums)), reverse=True)
    if len(a) < 3:
        return a[0]
    else:
        return a[2]


print(thirdMax([1, 2]))
