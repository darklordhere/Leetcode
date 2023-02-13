class Solution:
    def permuteUnique(self, n: List[int]) -> List[List[int]]:
        l = []
        for i in permutations(n):
            if i not in l:
                l.append(i)
        return l