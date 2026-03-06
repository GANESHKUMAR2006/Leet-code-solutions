class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        last_min=-1
        last_max=-1
        bad=-1
        ans=0
        for i,v in enumerate(nums):
            if v<minK or v>maxK:
                bad=i
            if v==minK:
                last_min=i
            if v==maxK:
                last_max=i
            ans+=max(0,min(last_min,last_max)-bad)
        return ans