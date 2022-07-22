class Solution:
    def romanToInt(self, s: str) -> int:
        final = []
        symbol = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        i = 0
        while i < len(s):
            if i + 1 > len(s) - 1:
                temp = symbol[s[i]]
                final.append(temp)
                break
            elif (s[i] == 'I' and s[i + 1] == 'V') or (s[i] == 'I' and s[i + 1] == 'X') \
                    or (s[i] == 'X' and s[i + 1] == 'L') or (s[i] == 'X' and s[i + 1] == 'C') \
                    or (s[i] == 'C' and s[i + 1] == 'D') or (s[i] == 'C' and s[i + 1] == 'M'):
                temp = symbol[s[i + 1]] - symbol[s[i]]
                i = i + 2
            else:
                temp = symbol[s[i]]
                i += 1
            final.append(temp)
        return sum(final)
