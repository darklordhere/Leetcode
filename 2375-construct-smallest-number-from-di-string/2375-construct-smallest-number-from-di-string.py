class Solution:
    def smallestNumber(self, p: str) -> str:
        p += 'I'
        r = s = ''
        for i,p in enumerate(p):
            s += str(i+1)
            if p == 'I':
                r += s[::-1]
                s =''
        return r