class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dp(i):
            if i == len(s): return 1
            if s[i] == '0': return 0
            return dp(i+1) + (dp(i+2) if 10 <= int(s[i:i+2]) <= 26 else 0)
        return dp(0)
