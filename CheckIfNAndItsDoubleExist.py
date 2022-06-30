from typing import List


def checkIfExist(arr: List[int]) -> bool:
    for i in range(len(arr)):
        print(arr[i])
        if arr[i] == 0 and arr[i] in arr[i:]:
            print(f'{arr[i]}  arr={arr[i + 1:]}')
            b = True
            break

        if (arr[i] % 2 == 0 and arr[i] / 2 in arr and arr[i] != 0) or (arr[i] * 2 in arr and arr[i] != 0):
            N, M = arr[i], arr[i] / 2
            print(f'{N}--{M}')
            b = True
            break
        b = False
    return b


print(checkIfExist([0, 0]))
