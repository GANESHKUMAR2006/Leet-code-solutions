class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n=len(nums)
        res=[0]*(n)
        for a in nums:
            if a>=n:
                return False
            if a<n-1 and res[a]==1:
                return False
            res[a]+=1
        return res[n-1]==2
