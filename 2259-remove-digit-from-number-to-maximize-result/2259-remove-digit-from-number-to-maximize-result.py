class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        r,n,d = 0,number,digit
        for i in range(len(n)):
            if n[i] == d:
                r = max((r,int(n[:i]+n[i+1:])))
        return str(r)