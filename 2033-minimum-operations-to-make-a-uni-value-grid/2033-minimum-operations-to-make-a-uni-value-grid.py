class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr=[]
        for r in grid:
            for c in r:
                arr.append(c)
        b=arr[0]
        for num in arr:
            if (num-b)%x!=0:
                return -1
        arr.sort()
        m=arr[len(arr)//2]
        op=0
        for num in arr:
            op+=abs(num-m)//x
        return op