class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        l = [stones.count(i) for i in jewels if i in stones]
        if l == []: return 0
        return sum(l)
        