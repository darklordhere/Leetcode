class Solution:
    def kthSmallest(self, m: List[List[int]], k: int) -> int:
        l = []
        for i in m:
            for j in i:
                l.append(j) 
        l = sorted(l)
        return l[k-1]