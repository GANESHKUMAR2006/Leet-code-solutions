class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        mylist=[]
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix)):
                mylist.append(matrix[i][j])
        mylist.sort()
        return mylist[k-1]