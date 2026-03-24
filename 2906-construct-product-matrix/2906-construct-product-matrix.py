class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        mod=12345
        ans=[[0]*n for _ in range(m)]
        suffix=1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                ans[i][j]=suffix
                suffix=(suffix*grid[i][j])%mod
        prefix=1
        for i in range(m):
            for j in range(n):
                ans[i][j]=(ans[i][j]*prefix)%mod
                prefix=(prefix*grid[i][j])%mod
        return ans