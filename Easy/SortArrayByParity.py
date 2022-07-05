from typing import List


def sortArrayByParity(nums: List[int]) -> List[int]:
    a, b = [], []
    for i in nums:
        print(i)
        if i % 2 == 0:
            a.append(i)
        else:
            b.append(i)
    a.extend(b)
    return a


print(sortArrayByParity([3, 1, 2, 4]))
