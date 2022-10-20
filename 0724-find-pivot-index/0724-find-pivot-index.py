class Solution:
    def pivotIndex(self, n: List[int]) -> int:
        s=sum(n)
        for i in range(len(n)):
            t=sum(n[:i])
            if t == s-t-n[i]:
                return i
        return -1