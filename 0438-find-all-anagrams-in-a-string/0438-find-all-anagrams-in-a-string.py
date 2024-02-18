class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i,j = 0,0
        l = []
        pc = Counter(p)
        
        while j < len(s):
#             x = s[i:j+1]
            
#             if len(x) < len(p):
#                 j += 1
#             elif len(x) == len(p):
#                 if Counter(x) == pc:
#                     l.append(i)
#                 i,j=i+1,j+1
                
            x = s[i:j+len(p)]
            
            if Counter(x) == pc:
                l.append(i)
            i,j=i+1,j+1
        return l
    