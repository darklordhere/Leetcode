class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        a, n = sorted(nums), len(nums) // 2
        return len({a[i] + a[~i] for i in range(n)})