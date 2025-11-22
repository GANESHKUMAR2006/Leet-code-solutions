class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        cnt=0
        n=len(nums)
        for i in range(n-1,1,-1):
            left=0
            right=i-1
            while left<right:
                if nums[right]+nums[left]>nums[i]:
                    cnt+=right-left
                    right-=1
                else:
                    left+=1
        return cnt