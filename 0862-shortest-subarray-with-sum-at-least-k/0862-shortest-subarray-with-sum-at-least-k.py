class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        from collections import deque
        dq=deque([])
        n=len(nums)
        pref=[0]*(n+1)
        for i in range(n):
            pref[i+1]=pref[i]+nums[i]
        ans=float('inf')
        dq=deque([])
        for i in range(n+1):
            while dq and pref[i]-pref[dq[0]]>=k:
                ans=min(ans,i-dq[0])
                dq.popleft()
            while dq and pref[i]<=pref[dq[-1]]:
                dq.pop()
            dq.append(i)
        return ans if ans!=float('inf') else -1
