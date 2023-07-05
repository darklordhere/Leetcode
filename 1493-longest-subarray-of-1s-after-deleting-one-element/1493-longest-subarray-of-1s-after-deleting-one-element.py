class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0 ; j = 0 ; n = len(nums) ; c = 0 ; mx = 0
        while j < n:
            if nums[j] == 0: c += 1
            while i < n and c == 2:
                if nums[i] == 0: c -= 1
                i += 1
            mx = max(j - i, mx) ; j += 1
        return mx
                




