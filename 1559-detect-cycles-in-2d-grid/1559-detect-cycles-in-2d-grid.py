class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows=len(grid)
        cols=len(grid[0])
        visit=[[False]*cols for _ in range(rows)]
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(r,c,pr,pc,char):
            visit[r][c]=True
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if 0<=nr<rows and 0<=nc<cols:
                    if grid[nr][nc]!=char:
                        continue
                    if nr==pr and nc==pc:
                        continue
                    if visit[nr][nc]:
                        return True
                    if dfs(nr,nc,r,c,char):
                        return True
            return False
        for r in range(rows):
            for c in range(cols):
                if not visit[r][c]:
                    if dfs(r,c,-1,-1,grid[r][c]):
                        return True
        return False