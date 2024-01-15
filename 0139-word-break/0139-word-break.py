class Solution:
    def wordBreak(self, s: str, wd: List[str]) -> bool:
        x = [False for _ in range(len(s)+1)]
        x[0] = True
        for i in range(len(s)):
            if x[i]:
                for j in wd:
                    if s[i:i+len(j)] == j:
                        x[i+len(j)] = True
        return x[-1]
        
        
#         x = s
#         sorted(wd)[::-1]
        
#         for i in wd:
#             if i in s:
#                 s = ",".join(s.split(i))
#         print(s)
#         print(set(list(s)))
#         if set(list(s)) != {','}:
            
#             return False
#             for i in wd:
#                 if i in x:
#                     x = ",".join(x.split(i))
#             if set(list(x)) != {','}:
#                 return False
#             else:
#                 return True
#         else:
#             return True