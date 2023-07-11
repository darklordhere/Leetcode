class Solution:
    def validPalindrome(self, s: str) -> bool:
        x,y = 0,len(s)-1
        while x < y:
            if s[x] != s[y]:
                a,b = s[x:y],s[x+1:y+1]
                return a==a[::-1] or b==b[::-1]
            x,y=x+1,y-1
        return True