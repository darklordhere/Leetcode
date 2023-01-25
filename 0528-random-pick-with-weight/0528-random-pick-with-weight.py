class Solution:

    def __init__(self, w: List[int]):
        self.w = w

    def pickIndex(self) -> int:
        return random.choices(range(len(self.w)), weights=self.w)[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()