class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        from collections import defaultdict
        ans=float('inf')
        dic=defaultdict(list)
        for i,val in enumerate(nums):
            dic[val].append(i)
            if len(dic[val])>=3:
                a,b,c=(dic[val])[-3:]
                dist=(abs(a-b)+abs(b-c)+abs(c-a))
                ans=min(ans,dist)
        if ans==float('inf'):
            return -1
        else:
            return ans