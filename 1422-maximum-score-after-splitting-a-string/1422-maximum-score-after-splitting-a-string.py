class Solution:
    def maxScore(self, s: str) -> int:
        def c1(s):
            x=0
            for i in s:
                if i == "0": x += 1
            return x
        m = 0
        for i in range(1,len(s)): m = max(c1(s[:i])+len(s[i:])-c1(s[i:]),m)
        return m