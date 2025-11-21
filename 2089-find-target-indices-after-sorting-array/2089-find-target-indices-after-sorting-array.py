class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l=len(nums)
        mylist=[]
        for i in range(0,l):
            if(nums[i]==target):
                mylist.append(i)
        return mylist