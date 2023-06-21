class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p = " "
        for i in strs:
            if (len(i) < len(p) or p == " "): p = i
        x = len(strs)
        c = 0 ; r = ""
        while (x!=c):
            c = 0
            for i in strs:
                if p == i[:len(p)]:
                    c+=1
            r = p
            p = p[:-1]
        if x == c:
            return r
        else:
            return ""