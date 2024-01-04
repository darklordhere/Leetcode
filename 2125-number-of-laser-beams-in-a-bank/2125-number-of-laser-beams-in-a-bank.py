class Solution:
    def numberOfBeams(self, b: List[str]) -> int:
        l = []
        for i in b:
            t = 0
            for j in i:
                if j == "1":
                    t += 1
            if t != 0:
                l.append(t)
        if len(l) == 1:
            return 0
        else:
            c = 0
            print(l)
            for i in range(len(l)-1):
                c += l[i]*l[i+1]
            return c