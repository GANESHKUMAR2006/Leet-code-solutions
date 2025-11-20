class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        mindiff=float('inf')
        for i in range(n-1):
            left=i+1
            right=n-1
            while left<right:
                s=nums[i]+nums[left]+nums[right]
                if abs(target-s)<abs(mindiff-target):
                    mindiff=s
                if s<target:
                    left+=1
                elif s>target:
                    right-=1
                else:
                    return s
        return mindiff