class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        f = 0
        s = 0
        for i in range(0,len(s1)):
            if s1[i] != s2[i]:
                if f == 0:
                    f = i
                elif s == 0:
                    s = i
                else:
                    return False
        return (s1[f] == s2[s]) and (s1[s] == s2[f])
