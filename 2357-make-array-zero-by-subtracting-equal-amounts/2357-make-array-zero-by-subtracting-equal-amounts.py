class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        from collections import Counter
        count=Counter(nums)
        counter=0
        for i in count.keys():
            if i!=0:
                counter+=1
        return counter