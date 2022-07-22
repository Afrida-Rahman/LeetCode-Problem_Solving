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
        print(f"left ones:{open} len={len(open)}")

        if len(open) == 1:
            print('when :: open ==== 1')
            return max(len(s) - 1 - open[0], len(s) - 1 - (len(s) - 1 - open[0]))
        elif len(open) > 1:
            print('when :: open > 1')
            for i in range(1, len(open)):
                length = max(length, open[i] - open[i - 1])
                print(f'Initial diff={open[i] - open[i - 1]}')
            length = max(len(s) - open[-1] - 1, length - 1)
            return max(open[0], length)
        else:
            print('when :: open ==== 0')
            return len(s)


s = "(()))())("
#    012345678
print(f"final result:: {s}  maxLength=" + str(Solution().longestValidParentheses(s)))
