class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        x = {}
        for i,j in enumerate(n):
            d = t-j
            if d in x:
                return [x[d],i]
            x[j] = i