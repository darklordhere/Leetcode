import numpy as np
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l = []
        for i in range(n+1):
            x = list(str(np.binary_repr(i,2)))
            l.append(x.count("1"))
            x = 0
        return l
        
        