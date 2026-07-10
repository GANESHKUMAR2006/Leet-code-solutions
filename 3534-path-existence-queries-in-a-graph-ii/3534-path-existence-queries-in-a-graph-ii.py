class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        arr=sorted((nums[i],i) for i in range(n))
        pos=[0]*n
        val=[0]*n
        for i,(x,idx) in enumerate(arr):
            val[i]=x
            pos[idx]=i
        comp=[0]*n
        cid=0
        for i in range(1,n):
            if val[i]-val[i-1]>maxDiff:
                cid+=1
            comp[i]=cid
        nxt=[0]*n
        r=0
        for i in range(n):
            while r+1<n and val[r+1]<=val[i]+maxDiff:
                r+=1
            nxt[i]=r
        log=n.bit_length()
        up=[nxt[:]]
        for _ in range(1,log):
            prev=up[-1]
            up.append([prev[prev[i]] for i in range(n)])
        ans=[]
        for u,v in queries:
            u=pos[u]
            v=pos[v]
            if u==v:
                ans.append(0)
                continue
            if comp[u]!=comp[v]:
                ans.append(-1)
                continue
            if u>v:
                u,v=v,u
            cur=u
            steps=0
            for k in range(log-1,-1,-1):
                if up[k][cur]<v:
                    cur=up[k][cur]
                    steps+=1<<k
            ans.append(steps+1)
        return ans