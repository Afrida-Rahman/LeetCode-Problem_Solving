from typing import List


#
# def check(n: int, s: List[str], a=None, i=0):
#     if a is None:
#         a = {'(': ')', '{': '}', '[': ']'}
#     while i < n:
#         # print(f"starting :: i={i}  s= {s} s[i]={s[i]}")
#         # print(f"i={i}  -- {a[s[i]]}  --  {s[i + 1]}  --  {s[n - i]}")
#         if i + 1 > n:
#             break
#         elif s[i] in list(a.values()):
#             i += 1
#         elif a[s[i]] == s[i + 1] and a[s[i]] == s[n - i]:
#             s.pop(i + 1)
#             s.pop(i)
#             n -= 2
#         elif a[s[i]] == s[i + 1]:
#             # print(f"entry in {a[s[i]]}, {s[i]}")
#             s.pop(i + 1)
#             s.pop(i)
#             n -= 2
#         elif a[s[i]] == s[n - i] and s[n - 1 - i] != s[i]:
#             s.pop(n - i)
#             s.pop(i)
#             n -= 2
#         elif a[s[i]] == s[n - i] and s[n - 1 - i] == s[i]:
#             i += 1
#         elif a[s[i]] != s[i + 1] and a[s[i]] != s[n - i] and a[s[i]] in s:
#             i += 1
#             # print(f"3 conditions:  i={i} ")
#         # else:
#         #     print(f"in else block={s} i={i}")
#         # print(f"nothing satisfy i={i}  s= {s}")
#     return s
#
#
# def isValid(s: str) -> bool:
#     s = list(s)
#     if len(s) % 2 == 0:
#         output = check(len(s) - 1, s)
#         if output:
#             output = check(len(output) - 1, output)
#         if not output:
#             return True
#         else:
#             return False
#     else:
#         return False

class Solution:

    def isValid(s: str) -> bool:
        m = list(s)
        if len(m) % 2 == 0:
            output = Solution.check(len(m) - 1, m)
            if len(output) < len(list(s)):
                print('checked')
                output = Solution.check(len(output) - 1, output)
            if not output:
                return True
            else:
                return False
        else:
            return False

    def check(n: int, s: List[str], a=None, i=0):
        c = 0
        if a is None:
            a = {'(': ')', '{': '}', '[': ']'}
        while i < n:
            if i + 1 > n:
                break
            elif s[i] in list(a.values()):
                print(f"A-values(): i={i} ")
                print(f"i={i} {s[i - 1]}  pre={a[s[i - 1]]} == s[i]={s[i]}")
                if i > 0 and a[s[i - 1]] == s[i]:
                    s.pop(i - 1)
                    i -= 1
                    s.pop(i)
                    n -= 2
                else:
                    i += 1
            elif a[s[i]] == s[i + 1] and a[s[i]] == s[n - i]:
                print(f"check next=last:  i={i} ")
                s.pop(i + 1)
                s.pop(i)
                n -= 2
            elif a[s[i]] == s[i + 1]:
                print(f"next:  i={i} ")
                s.pop(i + 1)
                s.pop(i)
                n -= 2
            elif a[s[i]] == s[n - i] and s[n - 1 - i] != s[i]:
                print(f"last and not same previous:  i={i} ")
                s.pop(n - i)
                s.pop(i)
                n -= 2
            elif a[s[i]] == s[n - i] and s[n - 1 - i] == s[i]:
                print(f"last and previous last same:  i={i} ")
                i += 1
                c += 1
            elif a[s[i]] != s[i + 1] and a[s[i]] != s[n - i] and a[s[i]] in s:
                print(f"not next, not last, but in s:  i={i} ")
                i += 1
                c += 1
            else:
                break
            print(s)
        return s


print(Solution.isValid("{[}[{}{{({)){[}([]{)}({())[}[}"))


# "(([]){})"
# [({(())}[()])]


class Solution:

    def isValid(s: str) -> bool:
        s = list(s)
        print(f"real s={s}")
        i = 0
        a = {'(': ')', '{': '}', '[': ']'}
        if len(s) % 2 == 0:
            print(len(s))
            while i < len(s) / 2:
                mid = int(len(s) / 2)
                print(s)
                # print(f"mid= {s[mid]} pre={a[s[mid]]} post={s[mid + 1]}")
                print(s[mid - 1])
                # if s[mid] in list(a.values()):
                #     print(f"A-values(): i={i} ")
                #     if s[mid] == a[s[mid - 1]]:
                #         s.pop(mid)
                #         s.pop(mid - 1)
                if s[mid - 1] not in list(a.values()) and a[s[mid - 1]] == s[mid - i]:
                    print(f"Enter:: mid= {mid}  pre={a[s[mid - 1]]}  post={s[mid - i]}")
                    s.pop(mid - 1)
                    mid -= 1
                    s.pop(mid)
                else:
                    if s[mid - 1] in list(a.values()):
                        print(f"A-values(): i={i} mid-1={s[mid - 2]} mid-2={s[mid - 1]} ")
                        if a[s[mid - 2]] == s[mid - 1]:
                            s.pop(mid - 1)
                            s.pop(mid - 2)
                    elif s[mid] in list(a.values()):
                        print(f"A-values(): i={i} mid-1={s[mid - 2]} mid-2={s[mid - 1]} ")
                        if a[s[mid - 1]] == s[mid]:
                            s.pop(mid)
                            s.pop(mid - 1)
                # elif a[s[mid]] == s[mid + 1]:
                #     s.pop(mid + 1)
                #     s.pop(mid)

        if not s:
            return True
        else:
            return False


print(Solution.isValid("[({(())}[()])]"))
# "(([]){})"
# [({(())}[()])]
# {[}[{}{{({)){[}([]{)}({())[}[}
