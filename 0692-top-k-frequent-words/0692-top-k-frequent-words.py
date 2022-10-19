class Solution:
    def topKFrequent(self, w: List[str], k: int) -> List[str]:
        x = Counter(w)
        print(x)
        l = sorted(x, key = lambda y: (-x[y],y))
        print(l)
        return (l[:k])
        