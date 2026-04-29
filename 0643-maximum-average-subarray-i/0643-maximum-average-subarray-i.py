class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0
        ans=float('-inf')
        pref=0
        for j in range(len(nums)):
            pref+=nums[j]
            while j-i+1>k:
                pref-=nums[i]
                i+=1
            if j-i+1==k:
                ans=max(ans,pref/k)
        return ans