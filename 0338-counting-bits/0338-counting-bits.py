class Solution:
    def countBits(self, n: int) -> List[int]:
        import numpy as np
        l = []
        for i in range(n+1): x = list(str(np.binary_repr(i,2)));l.append(x.count("1")) ;x = 0
        return l