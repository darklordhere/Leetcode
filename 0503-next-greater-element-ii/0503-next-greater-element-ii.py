class Solution:
    def nextGreaterElements(self, n: List[int]) -> List[int]:
        l = []
        ar = []
        for i in range(1,len(n)):
            if n[i] > n[0]:
                l.append(n[i]);break
        else:
            l.append(-1)
        for i in range(1,len(n)):
            x = n[i]
            if i == len(n)-1:
                for i in range(i):
                    if n[i] > x:
                        l.append(n[i]);break
                else:
                    l.append(-1)
            else:
                ar[:] = n[i+1:]+n[:i]
                for i in ar:
                    if i > x:
                        l.append(i);break
                else:
                    l.append(-1)
        return l
            