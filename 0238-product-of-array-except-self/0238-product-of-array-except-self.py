class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        lp=1
        left=[1]*n
        for i in range(n):
            left[i]=lp
            lp*=nums[i]
        rp=1
        right=[1]*n
        nums.reverse()
        for i in range(n):
            right[i]=rp
            rp*=nums[i]
        right.reverse()
        ans=[left[i]*right[i] for i in range(n)]
        return ans