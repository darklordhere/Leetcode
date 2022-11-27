class Solution:
    def pivotInteger(self, n: int) -> int:
        def f1(x):
            c = 0
            for i in range(1,x+1): c += i 
            return c
        def f2(x,n):
            c = 0
            for i in range(x,n+1): c += i
            return c
        if n == 1: return 1
        else:
            for i in range(1,n):
                if f1(i) == f2(i,n): return i ; break
            return -1
