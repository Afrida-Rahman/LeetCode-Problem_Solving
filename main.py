from typing import List


def validMountainArray1(arr: List[int]) -> bool:
    sortedList = sorted(arr, reverse=True)
    b = False
    for i in range(len(arr)):
        if i + 1 > len(arr) - 1:
            break
        else:
            if arr[0] == arr[len(arr) - 1]:
                if arr[i + 1] - arr[i] == 0:
                    b = False
                    break
                elif arr[0] > sortedList[0] and arr[len(arr) - 1] > sortedList[0]:
                    b = False
                    break
                elif arr[0] > sortedList[len(arr) - 1] and arr[len(arr) - 1] > sortedList[len(arr) - 1]:
                    b = False
                    break
                b = True
            elif arr[0] < sortedList[0] and arr[len(arr) - 1] < sortedList[0]:
                if arr[i + 1] - arr[i] == 0:
                    b = False
                    break
                elif arr[0] > sortedList[0] and arr[len(arr) - 1] > sortedList[0]:
                    b = False
                    break
                elif arr[0] > sortedList[len(arr) - 1] and arr[len(arr) - 1] > sortedList[len(arr) - 1]:
                    b = False
                    break
                b = True
            else:
                b = False
                break
    return b


def validMountainArray(arr: List[int]) -> bool:
    b = False
    inc = []
    dec = []
    a = sorted(arr, reverse=True)
    for i in arr[:arr.index(a[0])]:
        inc.append(i)
    for i in arr[arr.index(a[0]) + 1:]:
        dec.append(i)
    if sorted(inc, reverse=False) == inc and sorted(dec, reverse=True) == dec:
        for i in inc:
            if i + 1 > len(arr) - 1:
                break
            elif arr[i + 1] - arr[i] == 0:
                b = False
                break
        for j in dec:
            if j + 1 > len(arr) - 1:
                break
            elif arr[j + 1] - arr[j] == 0:
                b = False
                break
        b = True
    else:
        b = False
    return b


print(validMountainArray([5, 10, 12, 7, 5, 1, 2]))
