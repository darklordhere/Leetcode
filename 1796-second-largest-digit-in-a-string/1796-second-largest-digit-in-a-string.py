class Solution:
    def secondHighest(self, s: str) -> int:
        l = []
        for i in s:
            if i.isdigit():
                l.append(i)
        x = sorted(list(set(l)))
        print(x)
        if (len(x) == 1 ) or (l == []):
            return -1
        return x[-2]