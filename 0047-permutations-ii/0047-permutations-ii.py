class Solution:
    def permuteUnique(self, n: List[int]) -> List[List[int]]:
        return set([i for i in permutations(n)])