class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        pref=[0]*(n*2+1)
        pref[n]=1
        cnt=n
        ans=pre=0
        for i in range(n):
            if nums[i]==target:
                pre+=pref[cnt]
                cnt+=1
                pref[cnt]+=1
            else:
                cnt-=1
                pre-=pref[cnt]
                pref[cnt]+=1
            ans+=pre
        return ans