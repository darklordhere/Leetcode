class Solution:
    def findMatrix(self, n: List[int]) -> List[List[int]]:
        dic = {}
        for i in n:
            if i in dic: dic[i] += 1
            else: dic[i] = 1
        rr = []
        while dic:
            lis = [] ; 
            tem = []
            for i in dic:
                
                lis.append(i) ; dic[i] -= 1
                if dic[i] == 0: tem.append(i)
            rr.append(lis)
            
            for p in tem: del dic[p]
        return rr