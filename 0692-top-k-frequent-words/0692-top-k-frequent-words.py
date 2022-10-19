class Solution:
    def topKFrequent(self, w: List[str], k: int) -> List[str]:
        x = Counter(w)
        l = sorted(x, key = lambda y: (-x[y],y))
        return (l[:k])
        