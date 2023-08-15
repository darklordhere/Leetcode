class Solution:
    def kthSmallest(self, m: List[List[int]], k: int) -> int:
        l = sorted([j for i in m for j in i])
        # for i in m:
        #     l.extend(i)
        return l[k-1]