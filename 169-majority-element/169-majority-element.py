class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n,r,c = nums, nums[0] , 1
        for i in range(1,len(n)):
            if not c: r = n[i]
            if n[i] == r: c += 1
            else: c -= 1
        return r