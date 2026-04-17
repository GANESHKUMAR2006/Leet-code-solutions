class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def rev(x):
            return int(str(x)[::-1])
        mp={}
        ans=float('inf')
        for i,val in enumerate(nums):
            if val in mp:
                ans=min(ans,i-mp[val])
            r=rev(val)
            mp[r]=i
        return ans if ans!=float('inf') else -1