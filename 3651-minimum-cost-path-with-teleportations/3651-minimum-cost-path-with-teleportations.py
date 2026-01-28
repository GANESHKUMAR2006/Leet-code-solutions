class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        points=[]
        m,n=len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                points.append((i,j))
        points.sort(key=lambda p:grid[p[0]][p[1]])
        costs=[]
        for _ in range(m):
            costs.append([float('inf')]*n)
        for _ in range(k+1):
            minCost=float('inf')
            j=0
            total=len(points)
            i=0
            while i<total:
                r,c=points[i]
                minCost=min(minCost,costs[r][c])
                while (i+1<total and grid[points[i][0]][points[i][1]]==grid[points[i+1][0]][points[i+1][1]]):
                    i+=1
                    r,c=points[i]
                    minCost=min(minCost,costs[r][c])
                for x in range(j,i+1):
                    rr,cc=points[x]
                    costs[rr][cc]=minCost
                j=i+1
                i+=1
            for i in range(m-1,-1,-1):
                for j in range(n-1,-1,-1):
                    if i==m-1 and j==n-1:
                        costs[i][j]=0
                        continue
                    if i!=m-1:
                        costs[i][j]=min(costs[i][j],costs[i+1][j]+grid[i+1][j])
                    if j!=n-1:
                        costs[i][j]=min(costs[i][j],costs[i][j+1]+grid[i][j+1])
        return costs[0][0]
