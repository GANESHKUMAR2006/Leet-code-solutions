class Solution:
    def minElement(self, nums: List[int]) -> int:
        val=[]
        for i in nums:
            value=list(str(i))
            value=sum(int(values) for values in value)
            val.append(value)
        return min(val)