class Solution:
    def maxWidthOfVerticalArea(self, p: List[List[int]]) -> int:
        m = 0 ; p.sort()
        for i in range(1,len(p)): m = max(m,p[i][0]-p[i-1][0])
        return m