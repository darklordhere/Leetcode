class Solution:
    def updateMatrix(self, mat):
        ROW = len(mat)
        COL = len(mat[0])
        visited = set()
        q = deque()
        # Add all 0s to the queue and mark them vivisted 
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    visited.add((i,j))
                    q.append((i,j))
        
        while q:
            r,c = q.popleft()
            for row, col  in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_row = row+r
                new_col = col+c
                
                if 0<=new_row < ROW and 0<=new_col<COL and (new_row, new_col) not in visited:
                    #The new_row and new_col hasnt been marked vivisted yet means this is not zero 
                    #and this is this first time a cell is reaching it this means this r, c is its closest neighbor 
                    mat[new_row][new_col] = mat[r][c] + 1
                    visited.add((new_row, new_col))
                    q.append((new_row, new_col))
        return mat
                        
        