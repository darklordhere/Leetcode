class Solution:
    def sortColors(self, l: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def insertt(l,x):
            if (len(l)==0) or (l[len(l)-1]<=x):
                l.append(x)
                return l
            last = l[len(l)-1]
                # print(last)
            l.pop()
                # print(l)
            insertt(l,x)
            l.append(last)
            return l

        def f1(l):
            if len(l) == 1:
                return l
            x = l[len(l)-1]
                # print(x)
            l.pop()
                # print(l)
            f1(l)
            insertt(l,x)
            return l
        f1(l)