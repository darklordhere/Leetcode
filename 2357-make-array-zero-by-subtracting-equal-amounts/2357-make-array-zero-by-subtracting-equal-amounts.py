class Solution:
    def minimumOperations(self, n: List[int]) -> int:
        if 0 in set(n):
            return len(set(n))-1
        return len(set(n))