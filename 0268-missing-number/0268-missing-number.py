class Solution:
    def missingNumber(self, n: List[int]) -> int:
        return sum(range(len(n)+1))-sum(n)