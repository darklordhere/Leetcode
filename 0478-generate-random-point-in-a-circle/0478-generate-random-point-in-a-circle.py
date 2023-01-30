class Solution:

    def __init__(self, r: float, xc: float, yc: float):
        self.r = r
        self.xc = xc
        self.yc = yc

    def randPoint(self) -> List[float]:
        while True:
            x = random.uniform(self.xc-self.r,self.xc+self.r)
            y = random.uniform(self.yc-self.r,self.yc+self.r)
            if (x-self.xc)**2+(y-self.yc)**2 <= (self.r)**2:
                return [x,y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()