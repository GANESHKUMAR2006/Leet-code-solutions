class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*(n)
        left=0
        right=0
        for i in range(n):
            ans[i]=abs(ans[i]-left)
            ans[n-i-1]=abs(ans[n-i-1]-right)
            left+=nums[i]
            right+=nums[n-i-1]
        return ans