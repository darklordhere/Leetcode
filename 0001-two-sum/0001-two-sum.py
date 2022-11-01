class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        x = {}
        for i,j in enumerate(n):
            if t-j in x: return [x[t-j],i]
            x[j] = i