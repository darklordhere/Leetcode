class Solution:
    def largestPerimeter(self, n: List[int]) -> int:
        n.sort()
        for i in range(len(n)-3,-1,-1):
            if n[i] + n[i+1] > n[i+2]:
                return n[i]+n[i+1]+n[i+2]
        return 0