class Solution:
    def zeroFilledSubarray(self, n: List[int]) -> int:
        r = c = 0
        for i in n:
            if i == 0: 
                c += 1 
                r += c
            else: 
                c = 0
        return r