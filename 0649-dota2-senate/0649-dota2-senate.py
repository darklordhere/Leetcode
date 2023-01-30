class Solution:
    def predictPartyVictory(self, s: str) -> str:
        l = len(s)
        r = [i for i in range(l) if s[i] == 'R']
        d = [i for i in range(l) if s[i] == 'D']
        while len(d) and len(r):
            if d[0] > r[0]:
                r.append(r[0] + l)
            else: 
                d.append(d[0] + l)
            del d[0]
            del r[0]
        return "Dire" if len(d) != 0 else "Radiant"