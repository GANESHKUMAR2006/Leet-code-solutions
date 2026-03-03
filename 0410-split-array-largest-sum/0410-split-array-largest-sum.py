def check(arr,maxsum,m):
    pref=0
    stu=1
    for i in range(len(arr)):
        if arr[i]+pref>maxsum:
            pref=arr[i]
            stu+=1
            if stu>m:
                return False
        else:
            pref+=arr[i]
    return True
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)
        while low<=high:
            mid=(low+high)//2
            if check(nums,mid,k):
                high=mid-1
            else:
                low=mid+1
        return low