class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left=[]
        right=[]
        middle=[]
        for i in range(0,len(nums)):
            if(nums[i]<pivot):
                left.append(nums[i])
            elif(nums[i]==pivot):
                middle.append(nums[i])
            else:
                right.append(nums[i])
        return left+middle+right