class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}#dict
        for i,num in enumerate(nums):
            complement=target-num#sub the value and store in dict to see the value present in it
            if complement in seen:
                return [seen[complement],i]
                break
            seen[num]=i