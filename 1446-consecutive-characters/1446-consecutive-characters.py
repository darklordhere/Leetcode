class Solution:
    def maxPower(self, s: str) -> int:
        x,m = 1,1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                x += 1
            else:
                x = 1
            m = max(m,x)
        return m