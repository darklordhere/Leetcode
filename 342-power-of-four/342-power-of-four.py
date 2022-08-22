class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            while n > 1:
                n /= 4
            return n == 1