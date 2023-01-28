class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1: return 0
        m = 2**(n-1)//2
        return (int(self.kthGrammar(n-1,k)) if k<=m else int(1-self.kthGrammar(n-1,k-m)))
