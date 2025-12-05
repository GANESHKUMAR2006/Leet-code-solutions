class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        total=sum(nums)
        prefix=0
        for i in range(n-1):
            prefix+=nums[i]
            right=total-prefix
            if abs(right-prefix)%2==0:
                count+=1
        return count