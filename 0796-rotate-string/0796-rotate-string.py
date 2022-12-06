class Solution:
    def rotateString(self, s: str, g: str) -> bool:
        return len(s) == len(g) and g in s+s