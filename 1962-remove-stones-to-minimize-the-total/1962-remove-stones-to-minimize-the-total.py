class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        nums = [-num for num in piles]
        heapify(nums)
        
        while k:
            tmp = (-(heappop(nums)//2))
            heappush(nums, -tmp)
            k -= 1
        return -sum(nums)