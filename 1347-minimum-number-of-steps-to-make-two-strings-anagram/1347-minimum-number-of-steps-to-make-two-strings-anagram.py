class Solution:
    def minSteps(self, s: str, t: str) -> int:
        a,b = Counter(s),Counter(t)
        # print(a,b)
        c = 0
        for i in b:
            if i not in a:
                c += b[i]
            else:
                x,y = a[i],b[i]
                if x < y:
                    c += y-x
        return c