class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        pref=0
        left=0
        ans=float('inf')
        for right in range(len(nums)):
            pref+=nums[right]
            while pref>=target:
                ans=min(ans,right-left+1)
                pref-=nums[left]
                left+=1
        return 0 if ans==float('inf') else ans