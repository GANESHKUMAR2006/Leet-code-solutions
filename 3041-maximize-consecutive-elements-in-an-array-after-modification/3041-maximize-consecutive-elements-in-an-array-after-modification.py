class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        dp = {}
        for i in range(len(nums)):
            x = nums[i]
            dp[x+1] = max(dp.get(x+1,0),dp.get(x,0)+1)
            dp[x] = max(dp.get(x,0),dp.get(x-1,0)+1)
            ans = max(ans,dp[x+1],dp[x])
        return ans