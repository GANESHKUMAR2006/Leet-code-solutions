class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        string=""
        for i in nums:
            string=string+str(i)
        return [int(j) for j in string] 
        