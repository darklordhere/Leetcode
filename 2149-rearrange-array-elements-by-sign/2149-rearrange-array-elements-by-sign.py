class Solution:
    def rearrangeArray(self, n: List[int]) -> List[int]:
        a,b,r = [],[],[]
        for i in n:
            if i < 0: b.append(i)
            else: a.append(i)
        for i in range(len(a)): r.append(a[i]);r.append(b[i])
        return r
        