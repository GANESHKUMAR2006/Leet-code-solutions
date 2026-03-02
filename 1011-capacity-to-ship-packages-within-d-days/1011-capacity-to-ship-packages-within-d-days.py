def caldays(weights,capacity):
    load=0
    day=1
    for i in range(len(weights)):
        if load+weights[i]>capacity:
            load=weights[i]
            day+=1
        else:
            load+=weights[i]
    return day
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        while low<=high:
            mid=(low+high)//2
            day=caldays(weights,mid)
            if day<=days:
                high=mid-1
            else:
                low=mid+1
        return low
            