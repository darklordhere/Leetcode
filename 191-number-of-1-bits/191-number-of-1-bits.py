class Solution:
    def hammingWeight(self, n: int) -> int:
        x = 0
        while n:
            n &= n -1
            x += 1
        return x
    