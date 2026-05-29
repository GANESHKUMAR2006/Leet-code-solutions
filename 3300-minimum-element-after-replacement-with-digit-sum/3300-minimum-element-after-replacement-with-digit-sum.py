class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans=float('inf')
        for num in nums:
            newval=0
            while num>0:
                newval+=(num%10)
                num=num//10
            ans=min(ans,newval)
        return ans