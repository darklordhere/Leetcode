class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
#         def check(l):
#             for i in l:
#                 if i[1] > 0:
#                     return False
#             return True
        
#         x = Counter(s) ; l = []
#         # print(x)
#         for i,j in x.items():
#             l.append([i,j])
#         l = sorted(l)[::-1]
#         # print(l)
#         r = ''
#         while check(l) != True:
#             for i in l:
#                 if check(l):
#                     return r
#                 if r and r[-1] == i[0]:
#                     continue
#                 if i[1] <= repeatLimit:
#                     r += (i[0]*i[1])
#                     i[1] = 0
#                 if i[1] > repeatLimit:
#                     r += (i[0]*repeatLimit)
#                     i[1] -= repeatLimit
#         return r
        di = {}
        for i in s:
            di[i] = di.get(i, 0) + 1
        
        sorted_keys = sorted(di.keys())
        output = ""

        while sorted_keys:
            char = sorted_keys[-1]
            count = di[char]
            
            if count > repeatLimit: 
                output += char * repeatLimit
                di[char] -= repeatLimit
                
                if len(sorted_keys) > 1:
                    second_char = sorted_keys[-2]
                    output += second_char
                    di[second_char] -= 1
                    if di[second_char] == 0:
                        sorted_keys.pop(-2)
                else:
                    break
            else:
                output += char * count
                sorted_keys.pop()  
            
            if di[char] == 0 and sorted_keys:
                sorted_keys.pop()

        return output

        