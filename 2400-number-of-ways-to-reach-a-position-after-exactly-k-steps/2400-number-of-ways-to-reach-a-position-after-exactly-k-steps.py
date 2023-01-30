class Solution:
    def numberOfWays(self, s: int, e: int, k: int) -> int:
        if (s-e-k)%2:
            return 0
        return math.comb(k,((e-s)+k)//2)%(10**9+7)