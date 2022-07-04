from typing import List


def replaceElements(arr: List[int]) -> List[int]:
    a = []
    for i in range(len(arr)):
        if i + 1 > len(arr) - 1:
            a.append(-1)
            break
        else:
            a.append(max(arr[i + 1:]))
    return a


print(replaceElements([17, 18, 5, 4, 6, 1]))
