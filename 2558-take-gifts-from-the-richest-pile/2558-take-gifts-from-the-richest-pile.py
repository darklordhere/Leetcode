class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # while k != 0:
        #     gifts = sorted(gifts)[::-1]
        #     gifts[0] = int(math.sqrt(gifts[0]))
        #     k -= 1
        # return sum(gifts)
        
        nums = [-num for num in gifts]
        heapify(nums)
        
        while k:
            tmp = math.isqrt(-heappop(nums))
            heappush(nums, -tmp)
            k -= 1
            
        return -sum(nums)
        
        
        l = [-i for i in gifts]
        heapify(l)
    
        while k != 0:
            sqr = int(math.sqrt(-heappop(l)))
            heappush(l,-sqr)
            k -= 1
        return -sum(l)
      