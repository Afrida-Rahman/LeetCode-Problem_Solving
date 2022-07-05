from typing import List


def duplicateZeros(arr: List[int]) -> None:
    i = 0
    while i < len(arr) - 1:
        if arr[i] == 0 and arr[i + 1] != 0:
            arr.insert(i + 1, 0)
            arr.pop()
            i += 2
        elif arr[i] == 0 and arr[i + 1] == 0:
            arr.insert(i + 1, 0)
            arr.pop()
            i += 1
        i += 1
    print(arr)


print(duplicateZeros([1, 0, 0, 2, 0, 3, 0, 4, 5, 0]))
