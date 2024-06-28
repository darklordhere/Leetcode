class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        x = []
        nums.sort()
        a,b = 0,len(nums)-1
        while a < b:
            x.append((nums[a]+nums[b])/2)
            a += 1
            b -= 1
        return min(x)