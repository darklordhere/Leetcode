class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l = []
        for j in num:
            l.append(j)
        m = []
        l = [ int(x) for x in l]
        for i in range(2,len(l)):
            if l[i] == l[i-1] == l[i-2]:
                m.append(l[i])
        if m == []:
            return ""
        return (str((max(m)))*3)