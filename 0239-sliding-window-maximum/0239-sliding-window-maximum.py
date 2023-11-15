class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = []
        r = []
        for i,c in enumerate(nums):
            while q and nums[q[-1]] <= c:
                q.pop()
            q.append(i)
            if q[0] == i-k:
                q.pop(0)
            if i >= k-1:
                r.append(nums[q[0]])
        return r