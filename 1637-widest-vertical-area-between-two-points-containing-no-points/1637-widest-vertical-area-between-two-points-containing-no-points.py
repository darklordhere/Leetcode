class Solution:
    def maxWidthOfVerticalArea(self, p: List[List[int]]) -> int:
        m = 0
        x = [i[0] for i in sorted(p)]
        for i in range(1,len(p)):
            m = max(m,x[i]-x[i-1])
        return m