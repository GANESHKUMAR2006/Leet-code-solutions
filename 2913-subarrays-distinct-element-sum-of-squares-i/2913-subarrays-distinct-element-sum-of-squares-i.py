class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        for i in range(n):
            res=0
            seen=set()
            for j in range(i,n):
                if nums[j] not in seen:
                    seen.add(nums[j])
                    res+=1
                ans+=res*res
        return ans