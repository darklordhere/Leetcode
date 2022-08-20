class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        l = []
        for i in jewels:
            if i in stones:
                l.append(stones.count(i))
        if l == []:
            return 0
        return sum(l)