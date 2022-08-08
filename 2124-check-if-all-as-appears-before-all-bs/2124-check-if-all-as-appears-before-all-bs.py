class Solution:
    def checkString(self, s: str) -> bool:
        m = sorted(s)
        x = ''
        for i in m:
            x += i
        if x == s:
            return True
        return False