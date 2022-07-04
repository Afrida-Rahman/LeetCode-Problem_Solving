from typing import List


def heightChecker(heights: List[int]) -> int:
    c = 0
    a = sorted(heights, reverse=False)
    for i, j in zip(a, heights):
        print(f'i={i}  j={j}')
        if i != j:
            c += 1
    return c


print(heightChecker([1, 1, 4, 2, 1, 3]))
