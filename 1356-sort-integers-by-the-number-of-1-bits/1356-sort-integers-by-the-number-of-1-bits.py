class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        from collections import defaultdict
        mp=defaultdict(list)
        for value in arr:
            val=format(value,'b')
            mp[val.count('1')].append(value)
        ans=[]
        for j in sorted(mp.keys()):
            ans+=sorted(mp[j])
        return ans