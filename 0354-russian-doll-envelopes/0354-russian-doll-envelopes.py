class Solution:
    def maxEnvelopes(self, e: List[List[int]]) -> int:
        s = sorted(e,key= lambda x: (x[0],-x[1]))
        dp = []
        
        for w,h in s:
            i = bisect_left(dp,h)
            # i,l = 0,len(dp)
            # while i < l:
            #     if dp[i] >= h:
            #         break
            #     i += 1
            
            if i == len(dp):
                dp.append(h)
            else:
                dp[i] = h
                
        return len(dp)
        
        
        
#         l = []
#         c = 0
#         e = sorted(e)
#         print(e)
#         # def fnn(l):
#         #     for i in range(1,len(l)):
#         #         if l[i][1] > l[i][i-1]:
#         #             l.remove(l[i])
#         #     return l
            
            
#         def fn(l,i):
#             if l == []:
#                 l.append(i)
#             else:
#                 if l[-1][0] < i[0]:
#                     if l[-1][1] < i[1]:
#                         l.append(i)
#                     else:
                            
#                         for j in range(len(l)-1):
#                             if l[j][1] >= i[1]:
#                                 return l
#                         else:
#                             if l[-1][1] > i[1] and len(l) > 1 :
#                                 l[-1] = i
#                             else:
#                                 if l[-1][0] != i[0]:
#                                     l.append(i)
#                 elif l[-1][0] < i[0]:
#                     if l[-1][1] > i[1]:
#                         for j in l:
#                             if j[1] >= i[1]:
#                                 return l
#                         else:
#                             l[-1] = i
#                     else:
#                         l.append(i)
#             return l
#         for i in e:
#             l = fn(l,i)
#         print(l)
#         return len(l)
        