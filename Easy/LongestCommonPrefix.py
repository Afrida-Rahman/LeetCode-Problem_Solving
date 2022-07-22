from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        c = strs[0]
        for i in range(1, len(strs)):
            t = ""
            if len(c) == 0:
                break
            for j in range(len(strs[i])):
                if j < len(c) and c[j] == strs[i][j]:
                    t += c[j]
                else:
                    break
            c = t
        return c
