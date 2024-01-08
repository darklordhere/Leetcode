class Solution:
    def minMoves2(self, n: List[int]) -> int:
        x = [] 
        y = []
        c = 0
        n = sorted(n)
        if len(n)%2 == 0:
            m = n[len(n)//2-1]
        else:
            m = n[len(n)//2]
        for i in n:
            c += abs(i-m)
        return c
        