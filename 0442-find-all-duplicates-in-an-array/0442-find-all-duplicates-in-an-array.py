class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashset=set()
        ans=[]
        for i in nums:
            if i in hashset:
                ans.append(i)
            hashset.add(i)
        return ans