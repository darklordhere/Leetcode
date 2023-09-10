class Solution:
    def countOrders(self, n: int) -> int:
        mod=10**9+7
        x=n
        m=2*n-1
        res=1
        for i in range(2*n):
            if x!=0 and m!=0:
                res*=x
                res*=m
                x-=1
                m-=2
        return res%mod