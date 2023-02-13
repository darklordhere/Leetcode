class Solution:
    def countOdds(self, l: int, h: int) -> int:
        a,b = 0,0
        if l%2==0:
            a = (l//2)
        else:
            a = (l//2)
        if h%2 == 0:
            b = (h//2)
        else:
            b = (h//2)
        if l%2!=0 and h%2!=0 :
            return b-a+1
        elif l%2==0 and h%2!=0:
            return b-a+1
        else:
            return b-a