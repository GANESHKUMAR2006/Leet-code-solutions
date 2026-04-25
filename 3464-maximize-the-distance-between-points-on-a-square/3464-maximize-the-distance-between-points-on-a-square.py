class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        def convert(x,y):
            if x==0:
                return y
            elif y==side:
                return side+x
            elif x==side:
                return 3*side-y
            else:
                return 4*side-x
        arr=sorted([convert(x,y) for x,y in points])
        n=len(arr)
        pre=4*side
        ext=arr+[x+pre for x in arr]
        def can(d):
            for start in range(n):
                cnt=1
                idx=start
                first=ext[start]
                while cnt<k:
                    nxt=bisect_left(ext,ext[idx]+d,idx+1,start+n)
                    if nxt>=start+n:
                        break
                    idx=nxt
                    cnt+=1
                if cnt==k:
                    if pre-(ext[idx]-first)>=d:
                        return True
            return False
        low,high=0,2*side
        ans=0
        while low<=high:
            mid=(low+high)//2
            if can(mid):
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans