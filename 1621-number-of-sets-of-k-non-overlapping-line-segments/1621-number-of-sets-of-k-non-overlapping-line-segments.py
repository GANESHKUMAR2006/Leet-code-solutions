class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        mod=10**9+7
        dp=[[0]*(k+1) for _ in range(n)]
        dp[0][0]=1
        for i in range(n):
            dp[i][0]=1
        for j in range(1,k+1):
            prefix=0
            for i in range(n):
                if i>0:
                    prefix+=dp[i-1][j-1]
                    prefix%=mod
                dp[i][j]=dp[i-1][j] if i>0 else 0
                if i>0:
                    dp[i][j]+=prefix
                    dp[i][j]%=mod
        return dp[n-1][k]%mod