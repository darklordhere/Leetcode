class Solution:
    def trap(self, h: List[int]) -> int:
        s = 0
        x = [0]*len(h)
        # taking lenth of list for loop
        l, mlx , mrx = len(h) , [0]*len(h) , [0]*len(h)
        # finding max of left and right from index 0 and index -1
        mrx[0] , mlx[-1] = h[0] , h[-1]
        # looping through height to find max 
        for i in range(1,len(mrx)):
            mrx[i] = max(h[i],mrx[i-1])
        print(mrx)
        for i in range(len(mlx)-2,-1,-1):
            mlx[i] = max(mlx[i+1],h[i])
        print(mlx)
        for i in range(len(x)):
            x[i] = min(mlx[i], mrx[i])-h[i]
        return sum(x)