class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        ind = 0 ;i = 0; l = [i for i in range(n)]
        while ind < k:
            c = l[i]
            if i == 0:
                while i < len(l)-1:
                    if ind == k:
                        return c
                    i += 1
                    c = l[i]
                    ind += 1
            if i == len(l)-1:
                while i > 0:
                    if ind == k:
                        return c
                    i -= 1
                    c = l[i]
                    ind += 1
        return c 
                
                
