class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        from collections import deque
        dq=deque()
        dp=nums[:]
        for i in range(len(nums)):
            if dq:
                dp[i]=nums[i]+max(0,dp[dq[0]])
            while dq and dp[dq[-1]]<=dp[i]:
                dq.pop()
            dq.append(i)
            if dq[0]<=i-k:
                dq.popleft()
        return max(dp)