class Solution:
    def minMoves(self, nums: list[int]) -> int:
        moves = min(nums)
        n = len(nums)
        return sum(nums)-n*moves