class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        close_useless = 0
        temp = 0
        c = 0
        hold = 0
        open_count = 0
        total = 0
        for i in s:
            if i == '(':
                if open_count == 0 and temp < c:
                    temp = c
                    c = 0
                else:
                    open_count += 1
                    print('1st if')
                    stack.append(i)
            if i == ')':
                if not stack:
                    close_useless += 1
                    # print('not stack One' + i)
                    if temp < c:
                        temp = c
                        c = 0
                elif stack.pop() == '(':
                    total += 2
                    c += 2
                    open_count -= 1
            if not stack:
                print('no data')
            print(
                f"stack={stack} c={c} i={i} temp={temp} total={total} openCount={open_count}, closeCount={close_useless}")
        if len(stack) > 0:
            if temp < c:
                return c
            elif temp > c:
                return temp
        else:
            if close_useless <= 0:
                return total
            else:
                if temp < c:
                    return c
                elif temp > c:
                    return temp


s = "(()(()()()"
print(f"final result:: {s}" + str(Solution().longestValidParentheses(s)))
