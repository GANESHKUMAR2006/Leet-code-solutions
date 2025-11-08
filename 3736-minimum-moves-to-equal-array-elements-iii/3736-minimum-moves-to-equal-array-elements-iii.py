class Solution:
    def minMoves(self, nums: List[int]) -> int:
        cnt=0
        mx=max(nums)
        for i in nums:
            cnt+=mx-i
        return cnt