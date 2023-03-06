class Solution:
    def sortColors(self, n: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def f2(n,x):
            if len(n) == 0 or n[-1] <= x:
                n.append(x)
                return n
            y = n[-1]
            n.pop()
            f2(n,x)
            n.append(y)
        def f1(n):
            if len(n) == 1:
                return n
            x = n[-1]
            n.pop()
            f1(n)
            f2(n,x)
            return n
        return f1(n)