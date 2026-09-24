class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            value=str(nums[i])
            value=list(value)
            count=0
            for j in value:
                count+=int(j)
            if count==i:
                return i
                break
        return -1