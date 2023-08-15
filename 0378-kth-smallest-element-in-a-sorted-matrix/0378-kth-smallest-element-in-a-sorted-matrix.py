class Solution:
    def kthSmallest(self, m: List[List[int]], k: int) -> int:
        l = []
        for i in m:
            l.extend(i)
        l = sorted(l)
        return l[k-1]