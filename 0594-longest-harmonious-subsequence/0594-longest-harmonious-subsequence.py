class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq={}
        longest=0
        n=len(nums)
        for i in range(n):
            freq[nums[i]]=freq.get(nums[i],0)+1
        for val in freq:
            if val+1 in freq:
                longest=max(longest,freq[val]+freq[val+1])
        return longest