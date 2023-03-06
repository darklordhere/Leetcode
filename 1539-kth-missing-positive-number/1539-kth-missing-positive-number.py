class Solution:
    def findKthPositive(self, l: List[int], k: int) -> int:
        li = [] ; c = 0
        for i in range(1,5000):
            if c < k:
                if i not in l: c += 1
            else: return i-1