class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans=[]
        List=SortedList()
        for idx in range(len(nums)-1,-1,-1):
            pos=List.bisect_left(nums[idx])
            ans.append(pos)
            List.add(nums[idx])
        return ans[::-1]