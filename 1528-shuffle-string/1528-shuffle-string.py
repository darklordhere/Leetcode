class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        i = indices
        m = zip(i,s)
        l = []
        q = sorted(set(m))
        for j in q:
            l.append(j[1])
        return "".join(l)
        