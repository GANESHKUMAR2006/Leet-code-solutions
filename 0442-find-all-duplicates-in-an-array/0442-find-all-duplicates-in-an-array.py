class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        mp=defaultdict(int)
        for i in nums:
            mp[i]+=1
        ans=[]
        for i in mp.keys():
            if mp[i]==2:
                ans.append(i)
        return ans