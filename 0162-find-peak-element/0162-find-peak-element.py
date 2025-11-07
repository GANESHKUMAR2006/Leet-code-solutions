class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        mx=max(nums)
        for i in range (len(nums)):
            if(nums[i]==mx):
                return i
            
