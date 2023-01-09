class Solution:
    def subsetsWithDup(self, n: List[int]) -> List[List[int]]:
        l = [[]]
        for i in range(1,len(n)+1):
            x = combinations(n,i)
            for j in x:
                if sorted(j) not in l:
                    l.append(sorted(j))
        return l