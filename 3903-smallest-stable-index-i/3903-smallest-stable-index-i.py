class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        ans=float('inf')
        for i in range(len(nums)):
            ins=max(nums[:i+1])-min(nums[i:])
            if ins<=k:
                ans=min(ans,i)
        return ans if ans!=float('inf') else -1