class Solution:
    def isSameAfterReversals(self, n: int) -> bool:
        return str(n) == str(int(str(n)[::-1]))[::-1]