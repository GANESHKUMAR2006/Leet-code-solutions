class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n=len(grid)
        zero=[]
        for row in grid:
            count=0
            for i in range(n-1,-1,-1):
                if row[i]==0:
                    count+=1
                else:
                    break
            zero.append(count)
        swaps=0
        for i in range(n):
            required=n-i-1
            j=i
            while j<n and zero[j]<required:
                j+=1
            if j==n:
                return -1
            while j>i:
                zero[j],zero[j-1]=zero[j-1],zero[j]
                swaps+=1
                j-=1
        return swaps
