class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        x = itertools.permutations(nums)
        m = [i for i in x]
        return m