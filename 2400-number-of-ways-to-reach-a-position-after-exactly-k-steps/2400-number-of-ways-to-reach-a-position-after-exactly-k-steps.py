class Solution:
    def numberOfWays(self, s: int, e: int, k: int) -> int:
        return(0 if (s-e-k)%2 else comb(k,((e-s)+k)//2)%(10**9+7))