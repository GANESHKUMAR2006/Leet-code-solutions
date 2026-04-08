class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod=10**9+7
        for l,r,k,v in queries:
            idex=l
            while idex<=r:
                nums[idex]=(nums[idex]*v)%mod
                idex+=k
        ans=0
        for i in nums:
            ans^=i
        return ans