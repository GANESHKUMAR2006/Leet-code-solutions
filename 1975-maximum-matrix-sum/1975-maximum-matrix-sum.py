class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        minabs=float('inf')
        neg=0
        totalsum=0
        for arr in matrix:
            for val in arr:
                if val<0:
                    neg+=1
                av=abs(val)
                minabs=min(av,minabs)
                totalsum+=av
        return totalsum if neg%2==0 else totalsum-2*minabs