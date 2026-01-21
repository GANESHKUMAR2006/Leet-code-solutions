class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            if not i%2:
                ans.append(-1)
                continue
            n=(~i&(i+1)).bit_length()-1
            t=i-(1<<(n-1))
            ans.append(t)
        return ans