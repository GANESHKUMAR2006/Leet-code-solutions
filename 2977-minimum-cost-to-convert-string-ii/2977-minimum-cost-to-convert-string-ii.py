class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        inf=10**18
        inf_int=10**9
        n=len(source)
        child=[[-1]*26]
        tid=[-1]
        idx=-1
        def new_node():
            child.append([-1]*26)
            tid.append(-1)
            return len(child)-1
        def add(word):
            nonlocal idx
            node=0
            for ch in word:
                c=ord(ch)-97
                if child[node][c]==-1:
                    child[node][c]=new_node()
                node=child[node][c]
            if tid[node]==-1:
                idx+=1
                tid[node]=idx
            return tid[node]
        edges=[(add(o),add(c),w) for o,c,w in zip(original,changed,cost)]
        p=idx+1
        if p==0:
            return 0 if source==target else -1
        dist=[[inf_int]*p for _ in range(p)]
        for i in range(p):
            dist[i][i]=0
        for x,y,w in edges:
            dist[x][y]=min(dist[x][y],w)
        for k in range(p):
            for i in range(p):
                if dist[i][k]==inf_int:
                    continue
                for j in range(p):
                    nd=dist[i][k]+dist[k][j]
                    if nd<dist[i][j]:
                        dist[i][j]=nd
        dp=[inf]*(n+1)
        dp[0]=0
        s=[ord(c)-97 for c in source]
        t=[ord(c)-97 for c in target]
        for j in range(n):
            if dp[j]>=inf:
                continue
            if source[j]==target[j]:
                dp[j+1]=min(dp[j+1],dp[j])
            u=v=0
            for i in range(j,n):
                u=child[u][s[i]]
                v=child[v][t[i]]
                if u==-1 or v==-1:
                    break
                if tid[u]!=-1 and tid[v]!=-1:
                   w=dist[tid[u]][tid[v]]
                   if w!=inf_int:
                    dp[i+1]=min(dp[i+1],dp[j]+w)
        return -1 if dp[n]>=inf else dp[n]