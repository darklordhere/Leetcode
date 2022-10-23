class Solution:
    def findErrorNums(self, n: List[int]) -> List[int]:
        x = list(set([i for i in range(1,len(n)+1) ]) - set(n))
        y = mode(n)
        return [y,x[0]]
        # if x[0]-1 == 0:
        #     return [x[0]+1,x[0]]
        # else:
        #     return [x[0]-1,x[0]]
        # return 
        # for i in n:
        #     if n.count(i) == 2:
        #         x.insert(0,i)
        #         break
        # return x