class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        r,c = nums[0] , 1
        for i in range(1,len(nums)):
            if not c: r = nums[i]
            if nums[i] == r: c += 1
            else: c -= 1
        return r