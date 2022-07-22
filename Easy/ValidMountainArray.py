from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        b = False
        a = sorted(arr, reverse=True)
        inc = [i for i in arr[:(arr.index(a[0]) + 1)]]
        dec = [i for i in arr[arr.index(a[0]):]]

        if sorted(inc, reverse=False) == inc and len(inc) > 1 and len(dec) > 1 and sorted(dec, reverse=True) == dec:
            b = True
            for i in range(len(inc)):
                if inc.count(inc[i]) > 1:
                    b = False
                    break
            for i in range(len(dec)):
                if dec.count(dec[i]) > 1:
                    b = False
                    break
            if inc.count(0) > 1 and dec.count(0) > 1:
                b = False
        else:
            b = False
        return b
