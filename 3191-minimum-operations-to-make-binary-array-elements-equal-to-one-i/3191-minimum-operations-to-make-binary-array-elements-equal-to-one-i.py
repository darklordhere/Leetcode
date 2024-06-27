class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                nums[i] = 1-nums[i]
                nums[i+1] = 1-nums[i+1]
                nums[i+2] = 1-nums[i+2]
                c += 1
        if nums[-1] == nums[-2] == nums[-3] == 1:
            return c
        return -1