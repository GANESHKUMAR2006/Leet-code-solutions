class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def area(arr):
            arr.sort()
            max_len=cur=1
            for i in range(len(arr)-1):
                if arr[i]+1==arr[i+1]:
                    cur+=1
                else:
                    cur=1
                max_len=max(max_len,cur)
            return max_len
        h=area(hBars)
        v=area(vBars)
        s=min(h,v)+1
        return s*s