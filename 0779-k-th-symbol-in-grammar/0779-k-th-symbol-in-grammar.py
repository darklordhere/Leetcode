class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1:
            return 0
        m = (2**(n-1))//2
        if k <= m:
            return int(self.kthGrammar(n-1,k))
        else:
            return int(not self.kthGrammar(n-1,k-m))
