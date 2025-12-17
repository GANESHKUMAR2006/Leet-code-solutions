class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n=len(nums)
        ans=-1
        for i in range(n-1):
            for j in range(i,n):
                if i<j and nums[i]<nums[j] and ans<nums[j]-nums[i]:
                    ans=nums[j]-nums[i]
        return ans