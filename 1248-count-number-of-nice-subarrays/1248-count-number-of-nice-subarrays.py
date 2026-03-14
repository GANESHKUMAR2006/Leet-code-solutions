class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atmost(k):
            pref=0
            ans=0
            left=0
            for right in range(len(nums)):
                pref+=nums[right]%2
                while pref>k:
                    pref-=(nums[left]%2)
                    left+=1
                ans+=right-left+1
            return ans
        return atmost(k)-atmost(k-1)