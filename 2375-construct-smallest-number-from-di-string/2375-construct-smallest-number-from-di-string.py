class Solution:
    def smallestNumber(self, p: str) -> str:
        p += "I"
        t = ""
        r = ""
        for i,v in enumerate(p):
            t += str(i+1)
            if v == "I":
                r += t[::-1]
                t = ""
        return r