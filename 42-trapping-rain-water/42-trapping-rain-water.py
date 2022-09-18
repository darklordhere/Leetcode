class Solution:
    def trap(self, h: List[int]) -> int:
        lh= len(h) # initialising length of array
        # initialising list for updation 
        x , mlx , mrx = [0]*lh , [0]*lh , [0]*lh
        # To find max from left and right we initialise mrx , mlx
        mrx[0] , mlx[-1] = h[0] , h[-1]
        for i in range(1,len(mrx)):
            mrx[i] = max(h[i],mrx[i-1]) # max from right
        for i in range(len(mlx)-2,-1,-1):
            mlx[i] = max(mlx[i+1],h[i]) # max from left
        for i in range(len(x)):
            x[i] = min(mlx[i], mrx[i])-h[i] # for storing water unit/building
        return sum(x) #sum of all units
