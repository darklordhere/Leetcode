class Solution:
    def findFinalValue(self, n: List[int], o: int) -> int:
        for i in n:
            if o in n:
                o *= 2
        return o