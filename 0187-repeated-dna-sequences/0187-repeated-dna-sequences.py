class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l = set() ; m = set()
        for i in range(len(s)-9):
            x = s[i:i+10]
            if x in l and x not in m:
                m.add(x)
            else:
                l.add(x)
        # c = Counter(l)
        # m = []
        # for i in c:
        #     if c[i] > 1:
        #         m.append(i)
        return m