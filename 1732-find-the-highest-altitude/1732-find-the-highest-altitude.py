class Solution(object):
    def largestAltitude(self, g):
        r,a = 0,[0]
        for i in g: 
            r += i
            a.append(r)
        return max(a)