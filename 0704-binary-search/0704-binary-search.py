class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        if target not in nums:
            return -1
        elif len(nums) == 1 and nums[0] == target:
            return 0
        while l <= r:
            if nums[(l+r)//2] == target:
                return (l+r)//2
            elif nums[(l+r)//2] > target:
                r = ((l+r)//2)-1
            else:
                l = ((l+r)//2)+1
