class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        Arr=[]
        for num in nums:
            idx=bisect_left(Arr,num)
            if idx==len(Arr):
                Arr.append(num)
            else:
                Arr[idx]=num
        return len(Arr)