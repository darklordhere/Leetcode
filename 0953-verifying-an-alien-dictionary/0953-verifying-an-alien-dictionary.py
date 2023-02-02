class Solution:
    def isAlienSorted(self, w: List[str], o: str) -> bool:
        t = "".maketrans(o,string.ascii_lowercase)
        for i in range(len(w)): w[i] = w[i].translate(t)
        return w == sorted(w)
        