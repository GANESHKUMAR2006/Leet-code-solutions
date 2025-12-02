class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for num in nums:
            new=[]
            for value in res:
                value=value+[num]
                new.append(sorted(value))
            for i in new:
                res.append(i)
        sets=set()
        for i in res:
            sets.add(tuple(i))
        return [list(i) for i in sets]
