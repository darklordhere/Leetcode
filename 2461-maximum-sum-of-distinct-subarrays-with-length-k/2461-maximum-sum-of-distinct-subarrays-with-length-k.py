class Solution:
    def maximumSubarraySum(self, n: List[int], k: int) -> int:
        m = 0
        j = 0
        i = 0
        s = 0
        d = {}
        while j < len(n):
            s += n[j]
            d[n[j]] = d.get(n[j],0)+1
            if j-i+1 == k:
                if len(d) == k:
                    m = max(m,s)
                s -= n[i]
                if d[n[i]] == 1:
                    del d[n[i]]
                else:
                    d[n[i]] = d.get(n[i])-1
                i += 1
            j += 1
        return m
            