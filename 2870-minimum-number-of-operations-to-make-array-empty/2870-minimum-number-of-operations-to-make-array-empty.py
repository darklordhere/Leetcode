class Solution:
    def minOperations(self, n: List[int]) -> int:
        # print(10//4)
        x = Counter(n)
        # print(x)
        m,n=0,0
        for i in x:
            if x[i] ==1:
                return -1
            else:
                m += ceil(x[i]/3)
        return m
    