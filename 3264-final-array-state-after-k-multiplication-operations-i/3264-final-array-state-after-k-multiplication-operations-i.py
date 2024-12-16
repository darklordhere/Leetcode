class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k:
            x = nums.index(min(nums))
            nums[x] = nums[x]*multiplier
            k -= 1
        return nums