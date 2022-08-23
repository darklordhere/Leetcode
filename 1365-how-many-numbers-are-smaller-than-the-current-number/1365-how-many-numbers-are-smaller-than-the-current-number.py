class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        x,l = 0 , []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    x += 1
            l.append(x)
            x = 0
        return l