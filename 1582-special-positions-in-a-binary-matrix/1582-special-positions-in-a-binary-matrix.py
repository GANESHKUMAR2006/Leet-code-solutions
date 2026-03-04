class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m=len(mat)
        n=len(mat[0])
        row1=[0]*m
        col1=[0]*n
        for row in range(m):
            for col in range(n):
                if mat[row][col]:
                    row1[row]+=1
                    col1[col]+=1
        count=0
        for row in range(m):
            for col in range(n):
                if mat[row][col]:
                    if row1[row]==1 and col1[col]==1:
                        count+=1
        return count