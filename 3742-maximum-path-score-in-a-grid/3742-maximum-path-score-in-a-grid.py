class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        def val(x):
            if x==0:
                return (0,0)
            elif x==1:
                return (1,1)
            else:
                return (2,1)
        neg=-10**9
        dp=[[[neg]*(k+1) for _ in range(n)] for _ in range(m)]
        s,c=val(grid[0][0])
        if c<=k:
            dp[0][0][c]=s
        for i in range(m):
            for j in range(n):
                score,cost=val(grid[i][j])
                if i==0 and j==0:
                    continue
                for ncost in range(cost,k+1):
                    prev=ncost-cost
                    best=neg
                    if i>0:
                        best=max(best,dp[i-1][j][prev])
                    if j>0:
                        best=max(best,dp[i][j-1][prev])
                    if best!=neg:
                        dp[i][j][ncost]=best+score
        ans=max(dp[m-1][n-1])
        return ans if ans!=neg else -1