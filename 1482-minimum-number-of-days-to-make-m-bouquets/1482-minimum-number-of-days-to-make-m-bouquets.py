def check(arr,day,m,k):
    count=0
    boq=0
    for num in arr:
        if num>day:
            boq+=(count//k)
            count=0
        else:
            count+=1
    boq+=(count//k)
    return boq>=m
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        left=min(bloomDay)
        right=max(bloomDay)
        if m*k>len(bloomDay):
            return -1
        while left<=right:
            mid=(left+right)//2
            if check(bloomDay,mid,m,k):
                right=mid-1
            else:
                left=mid+1
        return left
            