class Solution:
    def searchInsert(self, n: List[int], t: int) -> int:
        if t in n:
            return n.index(t)
        else:
            if t > n[-1]:
                return len(n)
            elif t < n[0]:
                return 0
            else:
                for i in n:
                    if i > t:
                        return n.index(i)
        