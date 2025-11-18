class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=1
        n=len(nums)
        current=1
        for i in range(1,n):
            if nums[i]!=nums[i-1]:
                nums[current]=nums[i]
                current+=1
                count=1
            else:
                count+=1
                if count<=2:
                    nums[current]=nums[i]
                    current+=1
        return current