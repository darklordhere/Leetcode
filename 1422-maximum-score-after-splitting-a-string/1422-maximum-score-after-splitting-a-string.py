class Solution:
    def maxScore(self, s: str) -> int:
        def c1(s):
            x,y=0,0
            for i in s:
                if i == "0": x += 1
            return x
        m = 0
        for i in range(1,len(s)):
            a = c1(s[:i])
            b = len(s[i:])-c1(s[i:])
            m = max(a+b,m)
        return m