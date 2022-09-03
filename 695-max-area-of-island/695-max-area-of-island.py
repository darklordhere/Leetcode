class Solution:
    def maxAreaOfIsland(self, g: List[List[int]]) -> int:
        row , col = len(g) , len(g[0])
        used = set()
        def dfs(r,c):
            if r < 0 or c < 0 or r == row or c == col or g[r][c] == 0 or (r,c) in used :
                return 0
            used.add((r,c))
            return (1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1))
        m = 0
        for r in range(row):
            for c in range(col):
                m = max(m,dfs(r,c))
        return m