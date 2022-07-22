class Solution:
    def intToRoman(num: int) -> str:
        final = ""
        exceptional = {900: 'CM', 400: 'CD', 90: 'XC', 40: 'XL', 9: 'IX', 4: 'IV'}
        normal = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V'}
        for n, e in zip(normal, exceptional):
            # print(f"num={num} n={n}  e={e}")
            if num <= 0:
                break
            if num == n:
                print(f"num == n: {num}>{n} normal[n]={normal[n]}")
                num = num - n
                final += normal[n]
                print(f"num={num}")
                if num == n:
                    num = num - n
                    final += normal[n]
            elif num > n:
                print(f"num > n: {num}>{n} normal[n]={normal[n]}")
                num = num - n
                final += normal[n]
                print(f"num={num}")
                if num > n:
                    num = num - n
                    final += normal[n]
            if num == e:
                print(f"num == e : {num}>{e}  exceptional[e]={exceptional[e]}")
                num = num - e
                final += exceptional[e]
                print(f"num={num}")
            elif num > e:
                if num == n or num > n:
                    num = num - n
                    final += normal[n]
                else:
                    print(f"num > e : {num}>{e}  exceptional[e]={exceptional[e]}")
                    num = num - e
                    final += exceptional[e]
                    print(f"num={num}")
            if num <= 3:
                if num == 3:
                    final += "III"
                elif num == 2:
                    final += "II"
                elif num == 1:
                    final += "I"
                break
        return final


print(Solution.intToRoman(81))
