class Solution:
    def floodFill(self, i: List[List[int]], sr: int, sc: int, c: int) -> List[List[int]]:
        # starting position
        start = i[sr][sc]
        self.dfs(i,sr,sc,c,start)
        return i
    def dfs(self,i,sr,sc,c,start):
        if ( sr < 0 or sr > len(i)-1 ) or ( sc < 0 or sc > len(i[0])-1 ) or ( i[sr][sc] != start ) or ( i[sr][sc] == c ):
            return
        i[sr][sc] = c
        self.dfs(i,sr+1,sc,c,start)
        self.dfs(i,sr-1,sc,c,start)
        self.dfs(i,sr,sc+1,c,start)
        self.dfs(i,sr,sc-1,c,start)



