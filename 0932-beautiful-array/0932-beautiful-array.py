class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        x = [1]
        while len(x) < n: 
            x = [i*2-1 for i in x]+[i*2 for i in x]
        return [i for i in x if i <= n]