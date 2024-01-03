class Solution:
    def findHighAccessEmployees(self, at: List[List[str]]) -> List[str]:
        i = 0 ; l1 = []
        for i in at:
            if i[0] not in l1: l1.append(i[0])
        l2 = [[] for i in range(len(l1))]
        for i in range(len(at)):
            l2[l1.index(at[i][0])].append(at[i][1])
        d = dict(zip(l1,l2))
        s = set()
        for i in d:
            d[i] = sorted(d[i])
        for i in d:
            for j in range(len(d[i])):
                for k in range(j+1,len(d[i])):
                    if abs(int(d[i][k])-int(d[i][j])) < 100 and abs(k-j) >= 2:
                        s.add(i)
        return s