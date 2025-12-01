class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for num in nums:
            new_subset=[]
            for value in res:
                new=value+[num]
                new_subset.append(new)
            for s in new_subset:
                res.append(s)
        return res