class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            nums[i]=nums[i]*nums[i]
        nums.sort(reverse=True)
        mid=n//2
        if n%2!=0:
            mid+=1
        value=0
        for i in range(n):
            if mid<=i:
                value-=nums[i]
            else:
                value+=nums[i]
        return value