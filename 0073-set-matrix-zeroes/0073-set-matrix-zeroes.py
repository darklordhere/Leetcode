class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r,c = [],[]
        for i in range(len(m)):
            if 0 in m[i]: r.append(i)
                
        for j in range(len(m)):
            for i in range(len(m[j])):
                if m[j][i] == 0: c.append(i)
                    
        for i in r: m[i] = [0]*len(m[i])
            
        for j in c:
            for i in range(len(m)): m[i][j] = 0 
        return m
                
            
            
                
            
            
            
            
        