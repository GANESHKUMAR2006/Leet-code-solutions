class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        mn=nums.index(min(nums))
        mx=nums.index(max(nums))
        left=min(mn,mx)
        right=max(mn,mx)
        f1=right+1
        f2=n-left
        f3=(n-right)+(left+1)
        return min(f1,f2,f3)
