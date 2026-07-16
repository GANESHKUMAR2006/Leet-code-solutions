import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        arr=[0]*len(nums)
        val=nums[0]
        for i in range(len(nums)):
            val=max(val,nums[i])
            arr[i]=math.gcd(nums[i],val)
        arr.sort()
        left=0
        right=len(arr)-1
        ans=0
        while left<right:
            ans+=gcd(arr[left],arr[right])
            left+=1
            right-=1
        return ans