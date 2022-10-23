class Solution:
    def findErrorNums(self, n: List[int]) -> List[int]:
        return [mode(n), list(set([i for i in range(1,len(n)+1) ]) - set(n))[0]]