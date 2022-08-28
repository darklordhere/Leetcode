class Solution:
    def runningSum(self, n: List[int]) -> List[int]:
        l = [ sum(n[:i+1]) for i in range(len(n)) ]
        return l