class Solution:
    def check(self, nums: List[int]) -> bool:
        string1=""
        for i in nums:
            string1+=str(i)+","
        nums.sort()
        string2=""
        for j in nums:
            string2+=str(j)+","
        return string1 in string2+string2