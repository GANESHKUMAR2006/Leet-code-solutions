class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        remainder=0
        newlist=[]
        for bit in nums:
            remainder=(remainder*2+bit)
            newlist.append(remainder%5==0)
        return newlist