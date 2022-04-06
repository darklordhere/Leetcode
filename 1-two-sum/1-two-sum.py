class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}
        for i in range(len(nums)):
            x[nums[i]] = i
        for i in range(len(nums)):
            req = target - nums[i]
            if ( req in x.keys() and x[req] != i ):
                return [i,x[req]]
        