class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        i = 0; l = [1]*n ;mod = (10**9)+7
        while i<k:
            cs = l[0]
            for j in range(1,len(l)):
                cs += l[j]
                l[j] = cs
            i += 1
        return l[-1]%mod
            