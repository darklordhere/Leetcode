class Solution:
    def mxm(self, l: List[int], sz: int) -> int:
        mf = float('-inf') ; jj = 0
        
        for i in range(sz):
            
            jj += l[i]
            if mf < jj: mf = jj
                
            if jj < 0: jj = 0
                
        return mf
    def maximumCostSubstring(self, s: str, cs: str, vs: List[int]) -> int:
        km = {} ;c = 'a'; km[c] = 1
        for i in range(1, 26): c = chr(ord(c) + 1) ; km[c] = i + 1
        for i in range(len(cs)): km[cs[i]] = vs[i]
        va = []
        for i in range(len(s)): va.append(km[s[i]])
        r = self.mxm(va, len(va))
        if r < 0: return 0
        else: return r


