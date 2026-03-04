class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        buy=[float('inf')]*(k+1)
        sell=[0]*(k+1)
        for p in prices:
            for i in range(1,k+1):
                buy[i]=min(buy[i],p-sell[i-1])
                sell[i]=max(sell[i],p-buy[i])
        return sell[k]
