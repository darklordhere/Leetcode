class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i,j = 0,0
        l = []
        pc = Counter(p)
        while j < len(s):
            x = s[i:j+1]
            c = Counter(x)
            if len(x) < len(p):
                j += 1
            elif len(x) == len(p):
                if c == pc:
                    l.append(i)
                j += 1
                i += 1
        return l
        
        # def fn(s):
        #     c = dict()
        #     for i in s:
        #         if i not in c:
        #             c[i] = 1
        #         else:
        #             c[i] += 1
        #     return c
        