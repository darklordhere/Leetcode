class Solution:
    def maxArea(self, h: List[int]) -> int:
        l = 0
        r = len(h)-1 ; m = 0
        while l < r:
            hl , hr = h[l] , h[r] ; c = min(hl,hr)*(r-l)
            if c > m: m = c
            if hl <= hr:
                
                l += 1
            if hr <= hl:
                
                r -= 1
        return m