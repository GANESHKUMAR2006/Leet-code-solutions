class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        v=set()
        def dfs(i):
            if i<0 or i>=len(arr) or i in v:
                return False
            if arr[i]==0:
                return True
            v.add(i)
            return dfs(i+arr[i]) or dfs(i-arr[i])
        return dfs(start)
        