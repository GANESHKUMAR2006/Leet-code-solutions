def check(arr,hrs):
    total=0
    for right in range(len(arr)):
        total+=ceil(arr[right]/hrs)
    return total
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        while low<=high:
            mid=(low+high)//2
            hrs=check(piles,mid)
            if hrs<=h:
                high=mid-1
            else:
                low=mid+1
        return low
