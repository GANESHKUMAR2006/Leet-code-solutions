class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        rows=len(grid)
        cols=len(grid[0])
        res=set()
        for r in range(rows):
            for c in range(cols):
                res.add(grid[r][c])
                size=1
                while True:
                    if r+2*size>=rows or c-size<0 or c+size>=cols:
                        break
                    s=0
                    x=r
                    y=c
                    for i in range(size):
                        s+=grid[x+i][y-i]
                    for i in range(size):
                        s+=grid[x+size+i][y-size+i]
                    for i in range(size):
                        s+=grid[x+2*size-i][y+i]
                    for i in range(size):
                        s+=grid[x+size-i][y+size-i]
                    res.add(s)
                    size+=1
        ans=sorted(res,reverse=True)
        return ans[:3]