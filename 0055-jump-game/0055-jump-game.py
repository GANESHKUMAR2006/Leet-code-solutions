class Solution:
    def canJump(self, nums: List[int]) -> bool:
        fuel=0
        for i in range(len(nums)):
            if i>fuel:
                return False
            fuel=max(fuel,i+nums[i])
        return True