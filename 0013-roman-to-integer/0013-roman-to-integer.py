class Solution:
    def romanToInt(self, s: str) -> int:
        x = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        t = 0
        for i in range(len(s)):
            if i+1 < len(s) and x[s[i]] < x[s[i+1]]: t -= x[s[i]]
            else:t += x[s[i]]
        return t