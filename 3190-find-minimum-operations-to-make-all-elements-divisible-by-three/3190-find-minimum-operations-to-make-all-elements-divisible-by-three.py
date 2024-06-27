class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = 0
        for i in range(len(nums)):
            if (nums[i]+1) % 3 == 0:
                s += 1
            elif (nums[i]-1) % 3 == 0:
                s += 1
            else:
                pass
        return s
                