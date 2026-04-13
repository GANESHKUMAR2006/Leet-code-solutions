class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        value=float('inf')
        for i in range(len(nums)):
            if nums[i]==target:
                value=min(value,abs(i-start))
        return value