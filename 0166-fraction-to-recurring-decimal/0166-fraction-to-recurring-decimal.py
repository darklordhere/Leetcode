class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        r = ''
        if n*d<0: r+='-'
        n = abs(n) ; d = abs(d) ; r+= str(n//d) ; c = n%d
        if c>0: r+='.'
        m = {}
        while c>0:
            if c in m: i = m[c] ; r = r[:i]+'('+r[i:] +')' ; return r
            else: m[c]=len(r) ; r+=str((c*10)//d) ; c = ((c*10)%d)
        return r