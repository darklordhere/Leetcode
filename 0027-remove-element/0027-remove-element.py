class Solution:
    def removeElement(self, n: List[int], v: int) -> int:
        while v in n:
            n.remove(v)
        else:
            return len(n)