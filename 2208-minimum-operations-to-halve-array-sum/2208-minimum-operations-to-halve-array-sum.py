class Solution:
    def halveArray(self, num: List[int]) -> int:
        nums = [-i for i in num]
        x = sum(num)
        m = x/2
        heapify(nums)
        k = 0
        while x > m :
            tmp = heappop(nums)
            x += tmp/2
            heappush(nums,tmp/2)
            k += 1
        return k