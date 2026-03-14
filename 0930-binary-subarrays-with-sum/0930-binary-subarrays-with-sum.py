class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atmost(goal):
            if goal<0:
                return 0
            pref=0
            left=0
            ans=0
            for right in range(len(nums)):
                pref+=nums[right]
                while pref>goal:
                    pref-=nums[left]
                    left+=1
                ans+=(right-left+1)
            return ans
        return atmost(goal)-atmost(goal-1)
