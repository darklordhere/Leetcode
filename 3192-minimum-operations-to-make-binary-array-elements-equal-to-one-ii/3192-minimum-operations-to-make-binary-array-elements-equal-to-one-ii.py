class Solution:
    def minOperations(self, nums: List[int]) -> int:
        r = 0
        x = 0
        for i in nums:
            if i == x:
                r += 1
                x = not x
        return r