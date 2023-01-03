class Solution:
    def longestConsecutive(self, n: List[int]) -> int:
        x = sorted(set(n))
        l = []
        c = 1
        r = 1
        if x == []:
            return 0
        else:
            p = x[0]
            for i in range(1,len(x)):
                if x[i] - p  == 1:
                    c += 1
                else:
                    c = 1
                r = max(r,c)
                p = x[i]
            return r