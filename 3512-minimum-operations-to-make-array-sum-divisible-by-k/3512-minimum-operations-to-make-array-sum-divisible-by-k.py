class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        tot=sum(nums)
        count=0
        while tot%k!=0:
            tot-=1
            count+=1
        return count