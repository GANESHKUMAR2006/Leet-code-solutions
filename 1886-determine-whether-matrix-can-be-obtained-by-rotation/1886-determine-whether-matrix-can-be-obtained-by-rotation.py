class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n=len(mat)
        for i in range(n):
            for j in range(i+1,n):
                mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
        for row in mat:
            row.reverse()
        if target==mat:
            return True
        for i in range(n):
            for j in range(i+1,n):
                target[i][j],target[j][i]=target[j][i],target[i][j]
        for row in target:
            row.reverse()
        if target==mat:
            return True
        for i in range(n):
            for j in range(i+1,n):
                target[i][j],target[j][i]=target[j][i],target[i][j]
        for row in target:
            row.reverse()
        if target==mat:
            return True
        for i in range(n):
            for j in range(i+1,n):
                target[i][j],target[j][i]=target[j][i],target[i][j]
        for row in target:
            row.reverse()
        if target==mat:
            return True
        return False
        