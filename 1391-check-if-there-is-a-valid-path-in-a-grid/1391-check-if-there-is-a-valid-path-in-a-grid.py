class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m,n=len(grid),len(grid[0])
        dir={
            1:[(0,-1),(0,1)],
            2:[(-1,0),(1,0)],
            3:[(0,-1),(1,0)],
            4:[(0,1),(1,0)],
            5:[(0,-1),(-1,0)],
            6:[(0,1),(-1,0)],  
        }
        q=deque([(0,0)])
        visit=set()
        visit.add((0,0))
        while q:
            x,y=q.popleft()
            if (x,y)==(m-1,n-1):
                return True
            for dx,dy in dir[grid[x][y]]:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n:
                    for rdx,rdy in dir[grid[nx][ny]]:
                        if nx+rdx==x and ny+rdy==y:
                            if(nx,ny) not in visit:
                                visit.add((nx,ny))
                                q.append((nx,ny))
        return False