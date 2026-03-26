from collections import Counter
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m,n=len(grid),len(grid[0])
        totalsum=sum(sum(row) for row in grid)
        count=Counter()
        for row in grid:
            for val in row:
                count[val]+=1
        top=Counter()
        topsum=0
        for i in range(m-1):
            for val in grid[i]:
                topsum+=val
                top[val]+=1
                count[val]-=1
            bottom=totalsum-topsum
            if topsum==bottom:
                return True
            diff=abs(topsum-bottom)
            if topsum>bottom:
                if top[diff]>0:
                    if i+1==1 or n==1:
                        if grid[0][0]==diff or grid[i][-1]==diff:
                            return True
                    else:
                        return True
            else:
                if count[diff]>0:
                    if m-(i+1)==1 or n==1:
                        if grid[i+1][0]==diff or grid[-1][-1]==diff:
                            return True
                    else:
                        return True
        leftc=Counter()
        totalc=Counter()
        for row in grid:
            for val in row:
                totalc[val]+=1
        left=0
        for j in range(n-1):
            for i in range(m):
                val=grid[i][j]
                left+=val
                leftc[val]+=1
                totalc[val]-=1
            right=totalsum-left
            if left==right:
                return True
            diff=abs(left-right)
            if left>right:
                if leftc[diff]>0:
                    if j+1==1 or m==1:
                        if grid[0][0]==diff or grid[-1][j]==diff:
                            return True
                    else:
                        return True
            else:
                if totalc[diff]>0:
                    if n-(j+1)==1 or m==1:
                        if grid[0][j+1]==diff or grid[-1][-1]==diff:
                            return True
                    else:
                        return True
        return False