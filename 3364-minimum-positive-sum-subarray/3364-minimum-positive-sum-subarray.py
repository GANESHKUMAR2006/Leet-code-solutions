class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        ans = float('inf')

        for k in range(l,r+1):
            L = 0
            size = k 
            pref = 0
            for R in range(n):
                pref+=nums[R]
                if R-L+1>size:
                    pref-=nums[L]
                    L+=1
                if l<=R-L+1<=r and pref>0:
                    ans = min(ans,pref)

        if ans==float('inf') or ans<0:
            return -1
                    
        return ans