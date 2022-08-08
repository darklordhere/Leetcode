class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        w1,w2,l = Counter(word1) , Counter(word2) , []
        for i in "abcdefghijklmnopqrstuvwxyz":
            l.append(abs(int(str(w1[i] - w2[i]))))
        if max(l)>3:
            return False
        return True