class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        hashset=set()
        for i in range(n-2):
            left=i+1
            right=n-1
            while left<right:
                s=nums[i]+nums[left]+nums[right]
                if s==0:
                    hashset.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif s<0:
                    left+=1
                else:
                    right-=1
        return [i for i in hashset]