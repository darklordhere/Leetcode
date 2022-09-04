class Solution:
    def missingNumber(self, n: List[int]) -> int:
        for i in range(0,len(n)+1):
            if i not in n:
                return i
    
        