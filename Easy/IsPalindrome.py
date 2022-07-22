class Solution:
    def isPalindrome(self, x: int) -> bool:
        c = ""
        for i in list(str(x))[::-1]:
            c = c + i
        if c == str(x):
            return True
        else:
            return False
