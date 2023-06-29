class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        if len(s) == 0: return ""
        elif len(s) == 1: 
            return s[0]
        else:
            s.sort() ; r = ""
            for i in range(len(min(s[0],s[-1]))):
                if s[0][i] != s[-1][i]: 
                    break
                else: 
                    r += s[0][i]
            return r