class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(k//2):
            top=x+i
            bottom=x+k-1-i
            for j in range(k):
                col=y+j
                grid[top][col],grid[bottom][col]=grid[bottom][col],grid[top][col]
        return grid