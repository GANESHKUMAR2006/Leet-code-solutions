class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums=set(nums)
        ans=k
        mul=1
        while ans*mul in nums:
            mul+=1
        return ans*mul