class DataStream:

    def __init__(self, value: int, k: int):
        self.v = value
        self.k = k
        self.r = 0

    def consec(self, num: int) -> bool:
        if num == self.v:
            self.r += 1
        else:
            self.r = 0
        return self.r >= self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)