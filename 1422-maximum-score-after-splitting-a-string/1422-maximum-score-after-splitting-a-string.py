class Solution:
    def maxScore(self, s: str) -> int:
        m = 0
        def c1(s):
            x = 0
            for i in s:
                if i == "0":
                    x += 1
            return x
        def c2(s):
            x = 0
            for i in s:
                if i == "1":
                    x += 1
            return x
        for i in range(1,len(s)):
            m = max(c1(s[:i])+c2(s[i:]),m)
        return m