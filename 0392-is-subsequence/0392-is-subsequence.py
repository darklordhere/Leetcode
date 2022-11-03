class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t):
            return False
        
        l=0
        r=0
        
        while l<len(s) and r<len(t):
            if s[l]==t[r]:
                l+=1
                r+=1
            elif s[l]!=t[r]:
                r+=1
        print(l,r)
        if l==(len(s)):
            return True
        return False