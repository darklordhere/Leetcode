class Solution:
    def maxProfit(self, n: List[int]) -> int:
        mxx,mn = 0,99999
        for i in n: mxx = max(mxx,i-mn);mn = min(mn,i)
        return mxx