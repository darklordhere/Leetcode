class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        xy = [1]
        while len(xy) < n: 
            xy = [i*2-1 for i in xy]+[i*2 for i in xy]
        return [i for i in xy if i <= n]