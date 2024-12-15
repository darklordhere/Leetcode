class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # def check(nums):
        #     if len(nums) == 1:
        #         return True
        #     else:
        #         # for i in range(len(nums)):
        #         #     for j in range(len(nums)):
        #         #         if abs(nums[i]-nums[j]) > 2:
        #         #             return False
        #         return abs(max(nums)-min(nums)) <= 2
        # c = 0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)+1):
        #         if check(nums[i:j]):
        #             c += 1
        # return c
        
        from sortedcontainers import SortedList
        sl = SortedList([])
        
        nums.append(-5)
        start = 0
        sl.add(nums[start])
        count = 0
        for i in range(1, len(nums)):
            added = nums[i]
            sl.add(added)
            while abs(added - sl[0]) > 2 or abs(added - sl[-1]) > 2:
                subArrays = len(sl) - 1
                count += subArrays
                sl.remove(nums[start])
                start += 1
        return count