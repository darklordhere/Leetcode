class Solution:
    def sortPeople(self, n: List[str], h: List[int]) -> List[str]:
        l = []
        d = dict(zip(h,n))
        x = sorted(d.items())[::-1]
        for i in x:
            l.append(i[1])
        return l