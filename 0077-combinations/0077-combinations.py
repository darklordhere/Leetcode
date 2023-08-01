class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return [i for i in combinations(range(1,n+1),k)]