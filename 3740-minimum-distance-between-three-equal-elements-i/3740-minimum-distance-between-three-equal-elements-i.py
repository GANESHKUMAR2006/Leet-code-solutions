class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        from collections import defaultdict
        dic=defaultdict(list)
        ans=float('inf')
        for i,num in enumerate(nums):
            dic[num].append(i)
            if len(dic[num])>=3:
                a,b,c=dic[num][-3:]
                dist=abs(a-b)+abs(b-c)+abs(c-a)
                ans=min(ans,dist)
        if ans==float('inf'):
            return -1
        else:
            return ans