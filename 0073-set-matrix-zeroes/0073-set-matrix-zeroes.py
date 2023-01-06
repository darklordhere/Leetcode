class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lr , lc , r , c = len(m) , len(m[0]) , set() , set()
        for i in range(lr):
            for j in range(lc):
                if m[i][j] == 0:
                    r.add(i)
                    c.add(j)
        for i in range(lr):
            for j in range(lc):
                if i in r or j in c:
                    m[i][j] = 0
        
        