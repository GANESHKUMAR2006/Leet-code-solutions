class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        ans=float('inf')
        for x in (0,need1,need2):
            cost=(x*costBoth+max(0,need1-x)*cost1+max(0,need2-x)*cost2)
            ans=min(ans,cost)
        return ans