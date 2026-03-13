class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def canFinish(time):
            total=0
            for w in workerTimes:
                l,r=0,mountainHeight
                while l<=r:
                    mid=(l+r)//2
                    if w*mid*(mid+1)//2<=time:
                        l=mid+1
                    else:
                        r=mid-1
                total+=r
                if total>=mountainHeight:
                    return True
            return total>=mountainHeight
            
        left=0
        right=min(workerTimes)*mountainHeight*(mountainHeight+1)//2
        ans=right
        while left<=right:
            mid=(left+right)//2
            if canFinish(mid):
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans