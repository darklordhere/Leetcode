class Solution:
    def letterCombinations(self, d: str) -> List[str]:
        
        dic = {
            "1":"","2":"abc","3":"def", "4":"ghi", "5":"jkl",
            "6":"mno", "7":"pqrs","8":"tuv","9":"wxyz"
        }
        
        r = []
        def bk(i,curr):
            if len(curr) == len(d):
                r.append(curr)
                return
            for c in dic[d[i]]:
                bk(i+1,curr+c)
        if d:
            bk(0,"")
        return r
            
#         x = combinations("".join([dic[i] for i in d]),len(d))
#         k = [dic[i] for i in d]
#         m = "".join(k)
#         # print(m)
#         r = []
#         for i in x:
#             if "".join(i) not in m:
#                 r.append("".join(i))
#         r = r[1:len(r)-1]
#         for i in range(len(k)):
#             t = ""
#             for j in range(i+1,len(k)):
#                 t += k[i][-1]
#                 t += k[j][0]
#                 if len(t) == 2:
#                     r.append(t)
#                     break
#         if d == "":
#             return []
#         elif len(d) == 1:
#             return list(dic[d])
#         else:
#             return r
        
        
        

        