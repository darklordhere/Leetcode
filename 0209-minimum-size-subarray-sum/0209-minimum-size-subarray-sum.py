class Solution:
    def minSubArrayLen(self, t: int, n: List[int]) -> int:
        if sum(n) < t:
            return 0
        s,l,ans = 0,0,len(n)
        for r,val in enumerate(n):
            s += val
            while s >= t:
                s -= n[l]
                ans = min(ans,r-l+1) ; l += 1
        return ans