class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        mod=10**9+7
        n=len(edges)+1
        g=[[] for _ in range(n+1)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        q=deque([(1,0)])
        vis=[False]*(n+1)
        vis[1]=True
        mxdepth=0
        while q:
            node,depth=q.popleft()
            mxdepth=max(depth,mxdepth)
            for nxt in g[node]:
                if not vis[nxt]:
                    vis[nxt]=True
                    q.append((nxt,depth+1))
        return pow(2,mxdepth-1,mod)