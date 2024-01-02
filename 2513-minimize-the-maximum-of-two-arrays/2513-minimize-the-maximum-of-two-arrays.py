class Solution:
    def minimizeSet(self, d1: int, d2: int, uc1: int, uc2: int) -> int:
        l,r = 2,10**10
        x = 0
        while l < r:
            m = (l+r)//2
            a = m - (m//d1) >= uc1
            b = m - (m//d2) >= uc2
            c = m - m//lcm(d1,d2) >= (uc1+uc2)
            if a and b and c:
                r = m
            else:
                l = m+1
        return l
                
        
        
        
        
        
        
        
        
        
        
        
#         c1 = 1 ; c2 = 1 ; a1 = [] ; a2 = [] ; m = uc1+uc2
#         y1 = 0 ; y2 = 0 ; b1 = [] ; b2 = [] ; w1 = uc1 ; w2 = uc2
#         if d1 < d2:
#             while (len(a1)+len(a2)) < m:
#                 if (c1%d1 != 0 ) and (uc1 > 0):
#                     a1.append(c1)
#                     uc1 -= 1
#                 else:
#                     x = c1
#                     if (x%d2 != 0 ) and (uc2 > 0):
#                         a2.append(x)
#                         uc2 -= 1
#                     else:
#                         if x%d1 != 0:
#                             a1.append(x)
#                             uc1 -= 1
#                 c1 += 1
#         else:
#             while (len(a1)+len(a2)) < m:
#                 if (c1%d2 != 0 ) and (uc2 > 0):
#                     a2.append(c1)
#                     uc2 -= 1
#                 else:
#                     x = c1
#                     if (x%d1 != 0 ) and (uc1 > 0):
#                         a1.append(x)
#                         uc1 -= 1
#                     else:
#                         if x%d2 != 0:
#                             a2.append(x)
#                             uc2 -= 1
#                 c1 += 1
#         y1 = max(a1+a2)
#         c2 = 0
#         if d1 > d2:
#             while (len(b1)+len(b2)) < m:
#                 if (c2%d1 != 0 ) and (w1 > 0):
#                     b1.append(c2)
#                     w1 -= 1
#                 else:
#                     xx = c2
#                     if (xx%d2 != 0 ) and (w2 > 0):
#                         b2.append(xx)
#                         w2 -= 1
#                     else:
#                         if xx%d1 != 0:
#                             b1.append(xx)
#                             w1 -= 1
#                 c2 += 1
#         else:
#             while (len(b1)+len(b2)) < m:
#                 if (c2%d2 != 0 ) and (w2 > 0):
#                     b2.append(c2)
#                     w2 -= 1
#                 else:
#                     xx = c2
#                     if (xx%d1 != 0 ) and (w1 > 0):
#                         b1.append(xx)
#                         w1 -= 1
#                     else:
#                         if xx%d2 != 0:
#                             b2.append(xx)
#                             w2 -= 1
#                 c2 += 1
        
#         # print(a1,a2)
#         y2 = max(b1+b2)
#         return max(y1,y2)
        
            