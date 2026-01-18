class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        row=[[0]*(c+1) for _ in range(r)]
        col=[[0]*c for _ in range(r+1)]
        diag=[[0]*(c+1) for _ in range(r+1)]
        anti=[[0]*(c+2) for _ in range(r+1)]
        for i in range(r):
            for j in range(c):
                x=grid[i][j]
                row[i][j+1]=row[i][j]+x
                col[i+1][j]=col[i][j]+x
                diag[i+1][j+1]=diag[i][j]+x
                anti[i+1][j]=anti[i][j+1]+x
        def rs(i,j,k):
            return row[i][j+k]-row[i][j]
        def cs(i,j,k):
            return col[i+k][j]-col[i][j]
        def ds(i,j,k):
            return diag[i+k][j+k]-diag[i][j]
        def ads(i,j,k):
            return anti[i+k][j]-anti[i][j+k]
        for k in range(min(r,c),1,-1):
            for i in range(r-k+1):
                for j in range(c-k+1):
                    target=rs(i,j,k)
                    if ds(i,j,k)!=target or ads(i,j,k)!=target:
                        continue
                    ok=True
                    for t in range(k):
                        if rs(i+t,j,k)!=target or cs(i,j+t,k)!=target:
                            ok=False
                            break
                    if ok:
                        return k
        return 1