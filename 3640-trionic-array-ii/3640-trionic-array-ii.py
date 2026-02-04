class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n=len(nums)
        ans=float('-inf')
        i=0
        while i<n:
            j=i+1
            res=0
            while j<n and nums[j-1]<nums[j]:
                j+=1
            p=j-1
            if p==i:
                i+=1
                continue
            res+=nums[p]+nums[p-1]
            while j<n and nums[j-1]>nums[j]:
                res+=nums[j]
                j+=1
            q=j-1
            if q==p or q==n-1 or(j<n and nums[j]<=nums[q]):
                i=q
                continue
            res+=nums[q+1]
            mxsum=0
            cur=0
            k=q+2
            while k<n and nums[k]>nums[k-1]:
                cur+=nums[k]
                mxsum=max(mxsum,cur)
                k+=1
            res+=mxsum
            mxsum=0
            cur=0
            for k in range(p-2,i-1,-1):
                cur+=nums[k]
                mxsum=max(mxsum,cur)
            res+=mxsum
            ans=max(ans,res)
            i=q
        return ans