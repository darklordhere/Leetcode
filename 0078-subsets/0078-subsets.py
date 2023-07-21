class Solution:
    def subsets(self, s: List[int]) -> List[List[int]]:
        return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
