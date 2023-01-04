class Solution:
    def longestPrefix(self, s: str) -> str:
        i = 1
        while True:
            if s[i:] == s[:-i]:
                return s[i:]
            i += 1