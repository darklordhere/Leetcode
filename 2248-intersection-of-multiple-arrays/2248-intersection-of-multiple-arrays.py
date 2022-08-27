class Solution:
    def intersection(self, n: List[List[int]]) -> List[int]:
        l,x = [] , []
        for i in n:
            for j in i:
                if j not in l:
                    l.append(j)
        for i in l:
            for j in n:
                if i not in j:
                    x.append(i)
                    break
        return sorted(list(set(l) - set(x)))