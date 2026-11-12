class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 1
        n = len(nums)
        for i in range(n):
            inc = 1
            dec = 1
            prev = nums[i]
            for j in range(i+1,n):
                if prev<nums[j]:
                    inc +=1
                    dec =1
                if prev>nums[j]:
                    inc = 1
                    dec +=1
                if prev == nums[j]:
                    inc = 1
                    dec = 1
                prev = nums[j]
                ans = max(ans,inc,dec)
        return ans