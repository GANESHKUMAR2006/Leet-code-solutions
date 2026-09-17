class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n=len(arr)
        best=[float('inf')]*n
        left=0
        cur=0
        ans=float('inf')

        for right in range(n):
            cur+=arr[right]
            while cur>target:
                cur-=arr[left]
                left+=1
            if cur==target:
                length=right-left+1
                if left>0 and best[left-1]!=float('inf'):
                    ans=min(ans,length+best[left-1])
                if right==0:
                    best[right]=length
                else:
                    best[right]=min(best[right-1],length)
            else:
                if right>0:
                    best[right]=best[right-1]
        return -1 if ans==float('inf') else ans