```
class Solution:
def distinctEchoSubstrings(self, s: str) -> int:
return len({s[i:j] for j in range(len(s)) for i in range(j) if s[i:j]==s[j:j+j-i] })
​
# class Solution:
#     def distinctEchoSubstrings(self, s: str) -> int:
#         c = 0
#         d=set()
#         for i in range(len(s)):
#             for j in range(i + 1,len(s)+1):
#                 if s[i:j]*2 in s:
#                     d.add(s[i:j]*2)
#         return len(d)
# class Solution:
#     def distinctEchoSubstrings(self, s: str) -> int:
#         li = []
#         l = len(s)
#         i = 0
#         while i != l:
#             for j in range(i+1,len(s)+1):
#                 if (s[i:j])*2 in s and (s[i:j]*2) not in li:
#                     li.append((s[i:j])*2)
#             i += 1
#         return len(li)
```