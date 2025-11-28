class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        hashset=set()
        n=len(nums)
        for i in range(n):
            hashset.add(nums[i])
        for i in range(n):
            rev=str(nums[i])[::-1]
            hashset.add(int(rev))
        return len(hashset)