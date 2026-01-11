class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        n=len(matrix[0])
        heights=[0]*(n)
        max_area=0
        for row in matrix:
            for i in range(n):
                if row[i]=="1":
                    heights[i]+=1
                else:
                    heights[i]=0
            s=[]
            for i in range(n+1):
                h=heights[i] if i<n else 0
                while s and h<heights[s[-1]]:
                    height=heights[s.pop()]
                    width=i if not s else i-s[-1]-1
                    max_area=max(max_area,height*width)
                s.append(i)
        return max_area

