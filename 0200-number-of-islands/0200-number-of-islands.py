def mark0(grid,i,j):
    m=len(grid)
    n=len(grid[0])
    if i<0 or j<0:
        return
    if i>=m or j>=n:
        return
    if grid[i][j]=='0':
        return
    grid[i][j]='0'
    mark0(grid,i-1,j)
    mark0(grid,i+1,j)
    mark0(grid,i,j-1)
    mark0(grid,i,j+1)
    return grid
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    count+=1
                    mark0(grid,i,j)
        return count