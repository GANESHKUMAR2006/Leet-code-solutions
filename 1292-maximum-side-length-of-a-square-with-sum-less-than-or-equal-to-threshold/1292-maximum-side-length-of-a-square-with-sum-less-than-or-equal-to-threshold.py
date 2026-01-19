class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m=len(mat)
        n=len(mat[0])
        pref=[[0]*(n+1) for _ in range(m+1)] 
        for i in range(m):
            for j in range(n):
                pref[i+1][j+1]=mat[i][j]+pref[i][j+1]+pref[i+1][j]-pref[i][j]
        def possible(k):
            for i in range(k,m+1):
                for j in range(k,n+1):
                    total=pref[i][j]-pref[i-k][j]-pref[i][j-k]+pref[i-k][j-k]
                    if total<=threshold:
                        return True
            return False
        low,high=0,min(m,n)
        ans=0
        while low<=high:
            mid=(low+high)//2
            if possible(mid):
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans