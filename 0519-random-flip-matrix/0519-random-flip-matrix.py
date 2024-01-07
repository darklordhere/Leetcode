class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.l = []

    def flip(self) -> List[int]:
        a = random.randint(0,self.m*self.n-1)
        while a in self.l:
            a = random.randint(0,self.m*self.n-1)
        self.l.append(a)
        return [a//self.n,a%self.n]
    
            

    def reset(self) -> None:
        self.l = []


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()