import bisect
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        minremove=n
        for i in range(n):
            maxallowed=nums[i]*k
            j=bisect.bisect_right(nums,maxallowed)
            length=j-i
            toremove=n-length
            minremove=min(minremove,toremove)
        return minremove
            