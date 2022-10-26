class Solution:
    def checkSubarraySum(self, x: List[int], k: int) -> bool:
        d = {0:-1}
        s = 0
        for i,n in enumerate(x):
            s += n
            r = s%k
            if r not in d:
                d[r] = i
            elif i- d[r] > 1:
                return True
        return False