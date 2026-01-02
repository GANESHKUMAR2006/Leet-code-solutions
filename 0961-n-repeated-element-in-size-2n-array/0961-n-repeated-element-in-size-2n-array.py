class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums.sort()
        right=1
        left=0
        while True:
            if right>=len(nums):
                break;
            elif nums[left]==nums[right]:
                return nums[left]
                break;
            else:
                left+=1
                right+=1