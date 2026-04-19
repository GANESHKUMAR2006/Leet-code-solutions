class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        prefixmx=[nums[0]]*(n+1)
        for i in range(1,n):
            prefixmx[i]=max(prefixmx[i-1],nums[i])
        suffixmn=[nums[-1]]*(n+1)
        for i in range(n-2,-1,-1):
            suffixmn[i]=min(suffixmn[i+1],nums[i])
        ans=float('inf')
        for i in range(n):
            if prefixmx[i]-suffixmn[i]<=k:
                ans=min(ans,i)
        return ans if ans!=float('inf') else -1