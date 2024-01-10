class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        x = [i for i in range(1,n+1)]
        i = 0
        while len(x) > 1:
            i = (i+k-1)%len(x)
            x.pop(i)
        return x[0]