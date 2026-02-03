class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n=len(nums)
        p=0
        while p+1<n and nums[p]<nums[p+1]:
            p+=1
        if p==0 or p>n-3:
            return False
        q=p
        while q+1<n and nums[q]>nums[q+1]:
            q+=1
        if q==p or q>=n-1:
            return False
        for i in range(q,n-1):
            if nums[i]>=nums[i+1]:
                return False
        return True