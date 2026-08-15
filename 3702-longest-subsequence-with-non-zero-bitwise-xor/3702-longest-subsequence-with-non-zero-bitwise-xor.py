class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total=0
        for i in nums:
            total^=i
        if total!=0:
            return len(nums)
        return (len(nums)-1) if any(x!=0 for x in nums) else 0