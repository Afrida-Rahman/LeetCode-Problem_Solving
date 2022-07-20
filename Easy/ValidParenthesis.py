""" Using recursive function"""


# def balanced(s, i=0, cnt=0):
#     if i == len(s): return cnt == 0
#     if cnt < 0: return False
#     if s[i] == "(" or "{" or "[":
#         return balanced(s, i + 1, cnt + 1)
#     elif s[i] == ")" or "}" or "]":
#         return balanced(s, i + 1, cnt - 1)
#     return balanced(s, i + 1, cnt)
#
#
# for s in ["[({(())}[()])]", "(([]){})", "{[}[{}{{({)){[}([]{)}({())[}[}"]:
#     print("{}: {}".format(s, balanced(s)))

class Solution:
    def isValid(self, sequence: str):
        stack = []
        opening = set('([{')
        closing = set(')]}')
        pair = {')': '(', ']': '[', '}': '{'}
        for i in sequence:
            if i in opening:
                stack.append(i)
            if i in closing:
                if not stack:
                    return False
                elif stack.pop() != pair[i]:
                    return False
                else:
                    continue
        if not stack:
            return True
        else:
            return False


# if __name__ == '__mainEasy__':
sequence = '(([]){})'
print(f'Is {sequence} valid ? : {Solution().isValid(sequence)}')
sequence1 = '{[()]}{]{}}'
print(f'Is {sequence1} valid ? : {Solution().isValid(sequence1)}')
