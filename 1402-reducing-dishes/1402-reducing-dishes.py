class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        ans=0
        total=0
        prefix=0
        satisfaction.sort()
        n=len(satisfaction)
        for i in range(n-1,-1,-1):
            prefix+=satisfaction[i]
            total+=prefix
            ans=max(ans,total)
        return ans