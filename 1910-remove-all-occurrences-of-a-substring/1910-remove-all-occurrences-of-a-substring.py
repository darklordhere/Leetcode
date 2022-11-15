class Solution:
    def removeOccurrences(self, s: str, p: str) -> str:
        i = 0 ; r = ""
        while i < len(s):
            r += s[i]
            if p in r: r = r.replace(p,"")
            i += 1
        return r