class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[int]) -> int:
        requests=[x for x in requests if x!=start]
        if not requests:
            return 0
        arr=sorted(requests)
        m=len(arr)
        pos=0
        while pos<m and arr[pos]<start:
            pos+=1
        arr.insert(pos,start)
        s=pos
        n=len(arr)
        inf=10**30
        dp=[[[inf,inf] for _ in range(n)] for _ in range(n)]
        dp[s][s][0]=0
        dp[s][s][1]=0
        for length in range(1,n+1):
            rem=n-length
            left=max(0,s-length+1)
            right=min(s,n-length)
            for l in range(left,right+1):
                r=l+length-1
                if dp[l][r][0]<inf:
                    if l>0:
                        dist=arr[l]-arr[l-1]
                        cost=dp[l][r][0]+dist*rem
                        dp[l-1][r][0]=min(dp[l-1][r][0],cost)
                    if r+1<n:
                        dist=arr[r+1]-arr[l]
                        cost=dp[l][r][0]+dist*rem
                        dp[l][r+1][1]=min(dp[l][r+1][1],cost)
                if dp[l][r][1]<inf:
                    if l>0:
                        dist=arr[r]-arr[l-1]
                        cost=dp[l][r][1]+dist*rem
                        dp[l-1][r][0]=min(dp[l-1][r][0],cost)
                    if r+1<n:
                        dist=arr[r+1]-arr[r]
                        cost=dp[l][r][1]+dist*rem
                        dp[l][r+1][1]=min(dp[l][r+1][1],cost)
        return min(dp[0][n-1][0],dp[0][n-1][1])