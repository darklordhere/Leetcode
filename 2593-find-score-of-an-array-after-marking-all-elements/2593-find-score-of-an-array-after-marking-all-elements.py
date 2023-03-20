class Solution:
    def findScore(self, nums: List[int]) -> int:
        seen = [0] * (len(nums) + 1)
        res = 0
        for a,i in sorted([a,i] for i,a in enumerate(nums)):
            if not seen[i]: 
                res += a
                seen[i] = seen[i - 1] = seen[i + 1] = 1
        return res