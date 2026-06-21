class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count=0
        spend=0
        costs.sort()
        for i in range(len(costs)):
            if spend+costs[i]<=coins:
                count+=1
                spend+=costs[i]
        return count