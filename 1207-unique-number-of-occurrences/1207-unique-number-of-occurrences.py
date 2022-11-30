class Solution:
    def uniqueOccurrences(self, a: List[int]) -> bool:
        x = Counter(a) ; l = set()
        for i,j in x.items():
            if j in l: return False
            l.add(j)
        return True