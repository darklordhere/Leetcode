class Solution:
    def numRollsToTarget(self, n: int, k: int, t: int) -> int:
        dp = [[None for i in range(t+1)] for j in range(n+1)]
        mod = 1000000007
        return self.dfs(n,k,t,mod,dp)

    def dfs(self,n,k,t,mod,dp):
        if n == 0:
            if t == 0:
                return 1
            return 0
        if t < 0:
            return 0
        if dp[n][t] != None :
            return dp[n][t]
        ans = 0
        for i in range(1,k+1):
            ans = (ans+self.dfs(n-1,k,t-i,mod,dp))%mod
        dp[n][t] = ans % mod
        return ans % mod