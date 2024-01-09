class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l = set() ; m = set()
        for i in range(len(s)-9):
            # x = s[i:i+10]
            m.add(s[i:i+10]) if s[i:i+10] in l and s[i:i+10] not in m else l.add(s[i:i+10])
                
        # c = Counter(l)
        # m = []
        # for i in c:
        #     if c[i] > 1:
        #         m.append(i)
        return m