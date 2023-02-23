class Solution:
    def countDigits(self, n: int) -> int:
        c = 0
        for i in str(n):
            if n%int(i)==0: c += 1
        return c