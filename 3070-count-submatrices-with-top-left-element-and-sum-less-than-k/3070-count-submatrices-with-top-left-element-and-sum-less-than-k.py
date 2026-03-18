class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        pref=[[0]*n for _ in range(m)]
        count=0
        for i in range(m):
            for j in range(n):
                pref[i][j]=grid[i][j]
                if i>0:
                    pref[i][j]+=pref[i-1][j]
                if j>0:
                    pref[i][j]+=pref[i][j-1]
                if i>0 and j>0:
                    pref[i][j]-=pref[i-1][j-1]
                if pref[i][j]<=k:
                    count+=1
        return count