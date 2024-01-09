class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l = []
        for i in range(len(s)-9):
            l.append(s[i:i+10])
        c = Counter(l)
        m = []
        for i in c:
            if c[i] > 1:
                m.append(i)
        return m