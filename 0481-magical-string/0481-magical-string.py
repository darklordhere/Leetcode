class Solution:
    def magicalString(self, n: int) -> int:
        x = [1,2,2]
        for i in range(2,n):
            x += x[i] * [3-x[-1]]
        return x[:n].count(1)
