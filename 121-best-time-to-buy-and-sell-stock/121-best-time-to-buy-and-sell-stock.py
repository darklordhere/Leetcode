class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = prices
        f = 0
        m = 0
        for i in range(1,len(p)):
            if p[i] < p[m]:
                m = i
            f = max(f,p[i]-p[m])
        return f

                