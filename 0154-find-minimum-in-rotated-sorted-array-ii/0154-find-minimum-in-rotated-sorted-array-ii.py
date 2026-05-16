class Solution:
    def findMin(self, n: List[int]) -> int:
        l=0
        r=len(n)-1
        ans=float('inf')
        while l<=r:
            m=(l+r)//2
            if n[l]==n[m]==n[r]:
                ans=min(ans,n[l])
                l+=1
                r-=1
                continue
            if n[l]<=n[m]:
                ans=min(ans,n[l])
                l=m+1
            else:
                ans=min(ans,n[m])
                r=m-1
        return ans