class Solution:
    def maxSubArray(self, n: List[int]) -> int:
        c = 0 ; m = -99999
        for i in n:
            c += i
            if c > m: 
                m = c
            if c < 0: 
                c = 0
        return m