class Solution:
    def shuffle(self, n: List[int], k: int) -> List[int]:
        l = [] ; i = 0
        while k != i: l.append(n[:k][i]) ; l.append(n[k:][i]) ; i += 1
        return l
        