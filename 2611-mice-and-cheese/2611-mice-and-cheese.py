class Solution:
    @staticmethod
    def compare(a, b): return a[0] > b[0]
    def miceAndCheese(self, r1: List[int], r2: List[int], k: int) -> int:
        l = [] ; ne = len(r1)
        for w in range(ne):
            l.append((r1[w] - r2[w], w))
        l.sort(key=lambda j: j[0], reverse=True) ; 
        
        r = 0
        for p in range(ne):
            if p < k: r += r1[l[p][1]]
            else: r += r2[l[p][1]]
        return r