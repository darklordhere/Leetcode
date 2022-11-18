class Solution:
    def isUgly(self, n: int) -> bool:
        c = 2
        if n in (2,3,5): return True
        if n <= 0: return False
        while n > 1:
            if n % c == 0 and c in (2,3,4,5): n /= c
            elif c not in (2,3,4,5): return False ; break
            else: c += 1
        return True
    
            