class Solution:
    def findSubarrays(self, n: List[int]) -> bool:
        x = set()
        for i in range(len(n)-1):
            s = n[i]+n[i+1]
            if s in x:
                return True
            else:
                x.add(s)
        return False