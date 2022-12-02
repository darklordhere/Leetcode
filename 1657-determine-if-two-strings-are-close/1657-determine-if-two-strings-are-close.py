class Solution:
    def closeStrings(self, w1: str, w2: str) -> bool:
        if len(w1) != len(w2):
            return False
        else:
            c1 = Counter(w1) ; c2 = Counter(w2)
            if c1.keys() == c2.keys() and sorted(c1.values()) == sorted(c2.values()):
                return True
            else:
                return False