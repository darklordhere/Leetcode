class Solution:
    def maxConsecutive(self, b: int, t: int, s: List[int]) -> int:
        a = [b-1] + sorted(s) + [t+1]
        return max(a[i]-a[i-1]-1 for i in range(1, len(a)))