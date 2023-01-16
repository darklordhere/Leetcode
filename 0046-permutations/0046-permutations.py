class Solution:
    def permute(self, n: List[int]) -> List[List[int]]:
        return [i for i in permutations(n)]