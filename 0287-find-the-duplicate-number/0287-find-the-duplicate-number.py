class Solution:
    def findDuplicate(self, n: List[int]) -> int:
        return mode(n)
        
        
#         for i in range(1,len(n)):
#             if n[i] in n[:i] or n[i] in n[i+1:]:
#                 return n[i]


        # i = 1
        # while i != len(n):
        #     if n[i] in n[:i] or n[i] in n[i+1:]: return n[i]
        #     else: i += 1
        
            