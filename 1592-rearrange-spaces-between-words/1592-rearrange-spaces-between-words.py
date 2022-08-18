class Solution:
    def reorderSpaces(self, text: str) -> str:
        t = text
        m,x = t.count(" ") , t.split()
        for i in t:
            if len(x) == 1:
                return x[0] + " "*m
            else:
                y = len(x) -1 
                p,q = m // y , m % y
                return (' '*p).join(x) + " "*q
        
    