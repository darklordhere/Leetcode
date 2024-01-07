class Solution:
    def countDistinct(self, n: List[int], k: int, p: int) -> int:
        def sub_array(n):
            l = set()
            for i in range(len(n)):
                for j in range(i+1,len(n)+1):
                    l.add(tuple(n[i:j]))
            return l
        l = sub_array(n)
        c = 0
        y = set()
        for i in l:
            t = 0
            for j in i:
                if j%p == 0:
                    t += 1
            if t <= k and i not in y:
                y.add(i)
                c += 1
            t = 0
        return c
                    
                
                
            