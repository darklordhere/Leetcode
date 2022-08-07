class Solution:
    def capitalizeTitle(self, title: str) -> str:
        s = title.split(" ")
        l , r = [], ''
        for i in s:
            if len(i) > 2:
                l.append(i.capitalize())
            else:
                l.append(i.lower())
        for j in l:
            r += j + ' '
        r = r.strip()
        return r