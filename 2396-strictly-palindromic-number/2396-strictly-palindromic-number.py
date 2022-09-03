import numpy as np
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        b = 2
        def base(b):
            x = np.base_repr(n, base=b)
            return x
        for i in range(0,n-1):
            if base(b) != base(b)[::-1]:
                return False
            else:
                b+=1
        return True
        