class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(lo,hi):
            if hi-lo<=1:
                return 0
            mid=(lo+hi)//2
            count=merge(lo,mid) + merge(mid,hi)
            j=mid
            for i in range(lo,mid):
                while j<hi and nums[i]>nums[j]*2:
                    j+=1
                count+=j-mid
            nums[lo:hi]=sorted(nums[lo:hi])
            return count
        return merge(0,len(nums))