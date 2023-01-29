class Solution:
    def missingNumber(self, n: List[int]) -> int:
        return sum([i for i in range(1,len(n)+1)])-sum(n)