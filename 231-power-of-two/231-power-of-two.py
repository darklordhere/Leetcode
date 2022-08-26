class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            while n > 1:
                n /= 2
            return n == 1
        