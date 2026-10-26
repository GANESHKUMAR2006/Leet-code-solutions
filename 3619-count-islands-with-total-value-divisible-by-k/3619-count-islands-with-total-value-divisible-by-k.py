class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        row,cols=len(grid),len(grid[0])
        visited=[[False for i in range(cols)] for j in range(row)]
        def dfs(r,c):
            if r<0 or r>=row or c<0 or c>=cols or grid[r][c]==0 or visited[r][c]:
                return 0
            visited[r][c]=True
            total=grid[r][c]
            total+=dfs(r+1,c)
            total+=dfs(r-1,c)
            total+=dfs(r,c+1)
            total+=dfs(r,c-1)
            return total
        count=0
        for i in range(row):
            for j in range(cols):
                if grid[i][j]>0 and not visited[i][j]:
                    island=dfs(i,j)
                    if island%k==0:
                        count+=1
        return count