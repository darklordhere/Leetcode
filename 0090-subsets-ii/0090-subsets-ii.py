class Solution:
    def subsetsWithDup(self, n: List[int]) -> List[List[int]]:
        l = []
        r = [[]]
        for i in range(1,len(n)+1):
            x = combinations(n,i)
            for j in x:
                if j not in l:
                    l.append(sorted(j))
                else:
                    pass
        for i in l:
            if i not in r:
                r.append(list(i))
            else:
                pass
        return r