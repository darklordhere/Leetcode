class Solution:
    def uniqueOccurrences(self, a: List[int]) -> bool:
        x = Counter(a)
        l = []
        for i,j in x.items():
            l.append(j)
        return sorted(l) == sorted(list(set(l)))