class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left=0
        from collections import defaultdict
        mp=defaultdict(int)
        ans=0
        for right in range(len(nums)):
            mp[nums[right]]+=1
            while mp[nums[right]]>k:
                mp[nums[left]]-=1
                if mp[nums[left]]==0:
                    del mp[nums[left]]
                left+=1
            ans=max(ans,right-left+1)
        return ans 