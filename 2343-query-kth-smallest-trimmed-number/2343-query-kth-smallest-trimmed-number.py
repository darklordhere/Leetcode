class Solution:
    def smallestTrimmedNumbers(self, n: List[str], q: List[List[int]]) -> List[int]:
        x = []
        for i in q:
            l = [int(j[len(j)-i[1]:]) for j in n] 
            m = sorted(l)[i[0]-1]
            if l.count(m) < 2: x.append(l.index(m))
            else:
                p = [ i for i in range(len(l)) if l[i] == m]
                x.append(p[i[0]-1-(sorted(l).index(m))])
        return x





# class Solution:
#     def smallestTrimmedNumbers(self, n: List[str], q: List[List[int]]) -> List[int]:

#         l = []
#         x = []
#         def fn(l,m,y):
#             i = 0
#             r = 0
#             while y > 0 and i < len(l):
#                 if l[i] == m:
#                     r = i
#                     y -= 1
#                     i += 1
#                 else:
#                     i += 1
#             return r
        
#         def fn1(l,m,y,z):
#             i = 0
#             r = 0
#             while y > 0 and i < z:
#                 if l[i] == m:
#                     r = i
#                     y -= 1
#                     i += 1
#                 else:
#                     i += 1
#             return r

#         for i in q:
#             l = [int(j[len(j)-i[1]:]) for j in n]  
#             m = sorted(l)[i[0]-1]
#             if l.count(m) > 1:
#                 # print(l,sorted(l),m,sorted(l)[i[0]-1])
#                 if i[0]%2==1:
#                     x.append(fn(l,m,i[0]))
#                 if i[0]%2==0:
#                     x.append(fn1(l,m,i[0],l.count(m)))
#             else:
#                 x.append(l.index(m))
#         return x