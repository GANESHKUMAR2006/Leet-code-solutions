class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn=min(nums)
        mx=max(nums)
        for i in range(1,mn+1):
            if(mn%i==0 and mx%i==0):
                c=i
        return c
        