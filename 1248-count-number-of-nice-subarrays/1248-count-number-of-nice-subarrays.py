class Solution:
    def numberOfSubarrays(self, n: List[int], k: int) -> int:
        c = 0
        ind = 0
        r = 0
        j = 0
        for i in range(len(n)):
            if n[i]%2 != 0:
                c += 1
                j = 0
            while c == k and ind <= i:
                if n[ind]%2 != 0:
                    c -= 1
                ind += 1
                j += 1
            r += j
        return r