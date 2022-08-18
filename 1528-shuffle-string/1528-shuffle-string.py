class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        i,l = indices , []
        m = zip(i,s)
        q = sorted(set(m))
        for j in q:
            l.append(j[1])
        return "".join(l)
        