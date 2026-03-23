class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dp=[[(0,0)]*n for _ in range(m)]
        dp[0][0]=(grid[0][0],grid[0][0])
        for j in range(1,n):
            val=grid[0][j]
            mx,mn=dp[0][j-1]
            dp[0][j]=(mx*val,mn*val)
        for i in range(1,m):
            val=grid[i][0]
            mx,mn=dp[i-1][0]
            dp[i][0]=(mx*val,mn*val)
        for i in range(1,m):
            for j in range(1,n):
                val=grid[i][j]
                tmx,tmn=dp[i-1][j]
                lmx,lmn=dp[i][j-1]
                candidates=[tmx*val,tmn*val,lmx*val,lmn*val]
                dp[i][j]=(max(candidates),min(candidates))
        res=dp[m-1][n-1][0]
        if res<0:
            return -1
        return res%(10**9+7)