class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x = iter(t) ; return all(i in x for i in s)