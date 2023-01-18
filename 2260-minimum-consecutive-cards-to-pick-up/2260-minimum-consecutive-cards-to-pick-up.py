class Solution:
    def minimumCardPickup(self, c: List[int]) -> int:
        m = inf
        d = {}
        for i,j in enumerate(c):
            if j in d:
                m = min(m,i-d[j]+1)
            d[j] = i
        if m == inf:
            return -1
        return m