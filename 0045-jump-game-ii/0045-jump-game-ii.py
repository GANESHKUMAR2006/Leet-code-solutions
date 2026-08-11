class Solution:
    def jump(self, nums: List[int]) -> int:
        jump=0
        target=len(nums)-1
        while target!=0:
            for i in range(target):
                if i+nums[i]>=target:
                    target=i
                    jump+=1
                    break
        return jump