class Solution:
    def maxProfit(self, n: List[int]) -> int:
        mx,mn = 0,99999
        for i in n: mx = max(mx,i-mn);mn = min(mn,i)
        return mx