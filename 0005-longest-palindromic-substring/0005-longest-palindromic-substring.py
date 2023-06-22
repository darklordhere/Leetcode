class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]: return s
        else:
            x = []
            for i in range (len(s)):
                for j in range(i,len(s)):
                    if s[i:j+1] == s[i:j+1][::-1]: x.append(s[i:j+1])
            return max(x,key = len)
        
        
        '''
        N = len(s)
        dp=collections.defaultdict(bool)
        lp = []
        
        for i in range(N):
            dp[i,i] = True
            lp = [i,i]
        
        for inc in range(1, N+1):
            for i in range(N-inc):
                j = i+inc
                if s[i] == s[j] and (dp[i+1,j-1] or j-i==1):
                    dp[i,j] = True
                    if j-i+1 >  lp[1]-lp[0]+1:
                        lp =  [i,j]
        
        return s[lp[0]:lp[1]+1]
        '''