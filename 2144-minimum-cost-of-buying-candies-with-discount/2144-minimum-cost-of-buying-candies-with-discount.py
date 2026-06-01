class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost=sorted(cost)
        var=0
        for i in range(1,len(cost)+1):
            if(i%3!=0):
                var+=cost[-i]
        return var