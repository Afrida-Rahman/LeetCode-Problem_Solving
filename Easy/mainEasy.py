from typing import List


class Solution:

    def isValid(s: str) -> bool:
        s = list(s)
        print(f"real s={s}")
        i = 0
        a = {'(': ')', '{': '}', '[': ']'}
        mid = int(len(s) / 2)
        if len(s) % 2 == 0:
            print(len(s))
            if s[mid - 1] not in list(a.values()) and a[s[mid - 1]] == s[mid - i]:
                s = Solution.check(s, a)
            else:
                c = 0
                for i in range(int(len(s) / 2)):
                    print(f"before: {s[mid - i]}")
                    if s[mid - i] in list(a.values()):
                        print(f"after: {s[mid - i]} ind={mid - i}")
                        c += 1
                        ind = mid - i
                print(ind - c)
        if not s:
            return True
        else:
            return False

    def check(s: List[str], a=dict):
        i = 0
        while i < len(s) / 2:
            mid = int(len(s) / 2)
            print(s)
            print(f"Enter:: mid= {mid}  pre={a[s[mid - 1]]}  post={s[mid - i]}")
            s.pop(mid - 1)
            mid -= 1
            s.pop(mid)
        return s


print(Solution.isValid("[({(())}[()])]"))
# "(([]){})"
# [({(())}[()])]
# {[}[{}{{({)){[}([]{)}({())[}[}
