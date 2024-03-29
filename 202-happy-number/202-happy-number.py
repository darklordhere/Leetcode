class Solution:
    def isHappy(self, n: int) -> bool:
        x =  set()
        while n not in x:
            x.add(n)
            n = sum([int(i)**2 for i in str(n)])
        return n == 1