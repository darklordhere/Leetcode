class Solution:
    def reverse(self, x: int) -> int:
        x = str(x) ; r = -int(x[1:][::-1]) if x[0] == "-" else int(x[::-1])
        if r <= -(2**31) or r >= (2**31-1): return 0
        else: return r