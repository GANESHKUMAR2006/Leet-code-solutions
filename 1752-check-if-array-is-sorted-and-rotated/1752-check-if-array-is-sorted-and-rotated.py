class Solution:
    def check(self, nums: List[int]) -> bool:
        inv=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                inv+=1
                if inv>1:
                    return False
        if nums[0]<nums[-1]:
            inv+=1
        return inv<=1
        