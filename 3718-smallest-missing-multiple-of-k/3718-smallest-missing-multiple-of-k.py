class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n=len(nums)
        temp=[]
        for i in range(1,n+2):
            temp.append(k*i)
        for i in temp:
            if i in nums:
                continue
            else:
                return i
                break