import numpy as np
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return int("".join([format(i,"b") for i in range(1,n+1)]),2)%(10**9+7)