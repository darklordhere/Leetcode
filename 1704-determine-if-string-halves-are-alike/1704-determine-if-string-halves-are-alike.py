class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        f1,f2 = s[:len(s)//2] , s[len(s)//2:]
        c1 , c2 = 0,0
        v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in f1:
            if i in v:
                c1 += 1
        for j in f2:
            if j in v:
                c2 += 1
        return c1 == c2