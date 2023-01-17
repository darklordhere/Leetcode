class Solution:
    def findDuplicates(self, n: List[int]) -> List[int]:
        l = []
        for i,j in Counter(n).items():
            if j >= 2:
                l.append(i)
        return l