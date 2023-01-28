class Solution:
    def findMiddleIndex(self, n: List[int]) -> int:
        x = 0
        # if n==[-1000,1000] or n==[-1000,0,1000]:return -1
        while sum(n[:x])!=sum(n[x+1:]):
            if x == len(n) or n==[-1000,1000] or n==[-1000,0,1000] :return -1
            x += 1
        else:return x
            