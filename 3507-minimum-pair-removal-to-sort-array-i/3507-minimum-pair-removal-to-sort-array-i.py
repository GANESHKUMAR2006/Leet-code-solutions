class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops=0
        def sorting(a):
            return all(a[i]<=a[i+1] for i in range(len(a)-1))
        while not sorting(nums):
            bs=0
            for i in range(len(nums)-1):
                if nums[i]+nums[i+1]<nums[bs]+nums[bs+1]:
                    bs=i
            nums[bs]+=nums[bs+1]
            nums.pop(bs+1)
            ops+=1
        return ops