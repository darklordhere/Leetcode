class Solution:
    def searchInsert(self, n: List[int], t: int) -> int:
        x , y = 0 , len(n)-1
        while x<=y:
            m = (x+y)//2
            if n[m] == t:
                return m
            elif n[m] > t:
                y = m - 1
            else:
                x = m + 1
        return x
            