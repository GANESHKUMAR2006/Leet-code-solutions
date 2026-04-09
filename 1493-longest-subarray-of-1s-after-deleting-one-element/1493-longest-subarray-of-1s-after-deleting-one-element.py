class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k=1
        zero = 0
        left = 0
        ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero += 1
            if zero > k:
                if nums[left] == 0:
                    zero -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans-1
