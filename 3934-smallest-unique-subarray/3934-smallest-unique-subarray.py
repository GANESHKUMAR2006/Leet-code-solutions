class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        mod=(1<<61)-1
        base=911382323
        p=[1]*(n+1)
        pref=[0]*(n+1)
        for i in range(n):
            p[i+1]=(p[i]*base)%mod
            pref[i+1]=(pref[i]*base+nums[i]+1000007)%mod
        def mark(l,r):
            return (pref[r]-pref[l]*p[r-l])%mod
        def check(k):
            freq={}
            for i in range(n-k+1):
                h=mark(i,i+k)
                freq[h]=freq.get(h,0)+1
            for count in freq.values():
                if count==1:
                    return True
            return False
        low=1
        high=n
        ans=n
        while low<=high:
            mid=(low+high)//2
            if check(mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans