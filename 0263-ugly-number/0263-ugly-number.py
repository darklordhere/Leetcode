class Solution:
    def isUgly(self, n: int) -> bool:
        l=[2,3,4,5]
        dp=defaultdict()
        
        for i in l:
            dp[i]=1
        
        c = 2
        if n in (2,3,5): return True
        if n <= 0: return False
        while n > 1:
            if n % c == 0 and c in dp: n /= c
            elif c not in dp: return False ; break
            else: c += 1
        return True

    
            