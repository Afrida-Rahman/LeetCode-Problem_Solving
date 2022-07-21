class Solution:
    def longestValidParentheses(self, s: str) -> int:
        length = 0
        open = []
        close = []
        for i in range(len(s)):
            if s[i] == '(':
                open.append(i)
            else:
                if not open:
                    close.append(i)
                else:
                    open.pop()
            print(f"open={open}  close={close}")
        open.extend(close)
        open.sort()
        print(len(open))

        if len(open) == 1:
            print('hello' + str(len(s) - 1 - open[0]))
            return len(s) - 1 - open[0]
        elif len(open) > 1:
            for i in range(1, len(open)):
                length = max(length, open[i] - open[i - 1]) - 1
                print(f'Initial length={open[i] - open[i - 1]}')
            if len(s) - 1 - open[-1] > length:
                return len(s) - 1 - open[-1]
            else:
                return length
        else:
            return len(s)


s = "(()())()()())"
print(f"final result:: {s}  maxLength=" + str(Solution().longestValidParentheses(s)))
