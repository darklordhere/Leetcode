class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        a,b,c,d = 0,0,0,0
        for i in s:
            if i == '1':
                a += 1
                b = 0
            else:
                b += 1
                a = 0
            c = max(c,a)
            d = max(d,b)
        return c > d