class Solution:
    def rob(self, n: List[int]) -> int:
        a,b = 0,0
        for i in n:
            t = max(i+a,b)
            a = b
            b = t
        return b