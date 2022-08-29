class Solution:
    def rotate(self, n: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(n)
        x , y = 0 , len(n)-1
        while x < y:
            n[x],n[y] = n[y],n[x]
            x,y = x+1 , y-1
        x , y = 0 , k-1
        while x < y:
            n[x],n[y] = n[y],n[x]
            x,y = x+1 , y-1
        x , y = k , len(n)-1
        while x < y:
            n[x],n[y] = n[y],n[x]
            x,y = x+1 , y-1
        