class Solution:
    def nthUglyNumber(self, n: int) -> int:
        r = [1]
        a,b,c = 0,0,0
        while len(r) <= n:
            x = min(r[a]*2,r[b]*3,r[c]*5)
            r.append(x)
            if x == 2*r[a]: a += 1
            if x == 3*r[b]: b += 1
            if x == 5*r[c]: c += 1
        return r[n-1]
        
        