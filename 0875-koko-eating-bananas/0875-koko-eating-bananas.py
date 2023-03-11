class Solution:
    def minEatingSpeed(self, p: List[int], h: int) -> int:
        l = 1
        
        r = max(p)
        
        while l <= r:
            
            m = (l + r)//2
            t = sum([-(-i//m) for i in p])
            
            if t > h: l = m + 1
                
            else: r = m - 1
                
        return l