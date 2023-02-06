class Solution:
    def shuffle(self, n: List[int], k: int) -> List[int]:
        a,b = n[:k] , n[k:] ; l = [] ; i = 0
        while k != 0:
            l.append(a[i])
            l.append(b[i])
            i += 1
            k -= 1
        return l
        