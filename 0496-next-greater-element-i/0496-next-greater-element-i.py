class Solution:
    def nextGreaterElement(self, n1: List[int], n2: List[int]) -> List[int]:
        l = []
        for i in n1:
            x = n2.index(i)
            if x == len(n2)-1: l.append(-1)
            else:
                for j in range(x+1,len(n2)):
                    if n2[j] > n2[x]: l.append(n2[j]);break
                else: l.append(-1)
        return l