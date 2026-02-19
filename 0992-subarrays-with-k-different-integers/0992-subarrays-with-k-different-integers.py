def atmost(nums,k):
    left=0
    from collections import defaultdict
    mp=defaultdict(int)
    distinct=0
    res=0
    for right in range(len(nums)):
        mp[nums[right]]+=1
        if mp[nums[right]]==1:
            distinct+=1
        while distinct>k:
            mp[nums[left]]-=1
            if mp[nums[left]]==0:
                del mp[nums[left]]
                distinct-=1
            left+=1
        res+=(right-left+1)
    return res
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return atmost(nums,k)-atmost(nums,k-1)