class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    c.append((i,j))
        return len(c)
                    