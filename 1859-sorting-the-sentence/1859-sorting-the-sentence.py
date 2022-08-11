class Solution:
    def sortSentence(self, s: str) -> str:
        x, m , u = s.split(), [] , []
        for i in range(1,len(x)+1):
            m.append(i)
        for j in m:
            for k in x:
                if str(j) in k:
                    u.append(k[:-1])
        f = " ".join(u)
        return f
