class Solution:
    def threeConsecutiveOdds(self, l: List[int]) -> bool:
        for i in range(1,len(l)-1):
            if l[i-1]%2!=0 and l[i]%2!=0 and l[i+1]%2!=0:
                return True
        return False
                