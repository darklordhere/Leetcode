class Solution:
    def countEven(self, n: int) -> int:
        c = 0
        for i in range(2,n+1):
            i = str(i) ; l = [int(j) for j in i]
            if sum(l) % 2 == 0: c += 1
        return c
