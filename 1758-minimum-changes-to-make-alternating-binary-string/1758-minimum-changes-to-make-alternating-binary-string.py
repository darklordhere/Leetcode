class Solution:
    def minOperations(self, s: str) -> int:
        a = b = 0
        for i in range(len(s)):
            if i%2 ==0 :
                if s[i]=='0': a+=1
                else: b+=1
            else:
                if s[i]=='1': a+=1
                else: b+=1
        return min(len(s)-a,len(s)-b)