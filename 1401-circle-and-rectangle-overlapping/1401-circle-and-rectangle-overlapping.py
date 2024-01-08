class Solution:
    def checkOverlap(self, r: int, xc: int, yc: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        x = min(xc,x2)
        y = min(yc,y2)
        x = max(x1,x)
        y = max(y1,y)
        if (x-xc)**2 + (y-yc)**2 <= r**2:
            return True
        else:
            return False