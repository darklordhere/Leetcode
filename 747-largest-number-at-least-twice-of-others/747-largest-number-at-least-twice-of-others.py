class Solution(object):
    def dominantIndex(self, n):
        l = n
        l = sorted(l)
        r = l.pop()
        if r >= (l[-1])*2:
            return n.index(r)
        return -1
        
        