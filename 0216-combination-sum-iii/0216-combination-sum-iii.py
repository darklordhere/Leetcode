class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        x = combinations([i for i in range(1,10)],k)
        l = []
        for i in x:
            if sum(i) == n and sorted(i) not in l:
                l.append(sorted(i))
        return l