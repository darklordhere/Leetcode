class Solution:
    def search(self, n: List[int], t: int) -> int:
        if t in n: return n.index(t)
        return -1