class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        mp=defaultdict(int)
        mp[0]=1
        curr=0
        ans=0
        for i in nums:
            curr+=i%2
            ans+=mp[curr-k]
            mp[curr]+=1
        return ans