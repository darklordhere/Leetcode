class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        x = [ i**2 for i in nums ]
        return sorted(x)