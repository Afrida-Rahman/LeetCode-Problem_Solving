from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    t = 0
    c = 0
    for i in nums:
        if i == 1:
            t += i
            if c < t:
                c = t
        else:
            t=0
    return c


print(findMaxConsecutiveOnes([1,0,0,0,1,1,1,0,0,0,1,1,1,1,1,1,0,0,1,1,1]))