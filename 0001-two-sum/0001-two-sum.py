class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value=[]
        for i,val in enumerate(nums):
            value.append((val,i))
        nums=value
        nums.sort()
        left=0
        right=len(nums)-1
        while left<right:
            if nums[left][0]+nums[right][0]==target:
                return [nums[left][1],nums[right][1]]
            elif nums[left][0]+nums[right][0]>target:
                right-=1
            else:
                left+=1