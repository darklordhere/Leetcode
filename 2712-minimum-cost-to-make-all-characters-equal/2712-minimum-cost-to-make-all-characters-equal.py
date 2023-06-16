class Solution:
    def minimumCost(self, s: str) -> int:
        r = 0
        for i in range(1,(len(s)+1)//2):
            r += (s[i] != s[i-1])*i
        for i in range((len(s)+1)//2,len(s)):
            r += (s[i]!=s[i-1]) * (len(s)-i)
        return r