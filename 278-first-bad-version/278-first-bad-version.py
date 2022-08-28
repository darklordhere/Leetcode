# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        x,y = 1 , n
        while x <= y:
            m = (x+y)//2
            if m == 0:
                return 1
            if isBadVersion(m) == False:
                x = m+1
            else:
                y = m-1
        return x
        
                