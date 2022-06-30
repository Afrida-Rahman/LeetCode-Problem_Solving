from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    n1 = nums1[:m]
    nums1.clear()
    nums1.extend(n1)
    nums1.extend(nums2[:n])
    nums1.sort(reverse=False)


print(merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6, 0], n=3))
