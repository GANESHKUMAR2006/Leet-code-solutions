class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        import heapq
        from collections import defaultdict
        uedges=defaultdict(list)
        vedges=defaultdict(list)
        for u,v,w in edges:
            uedges[u].append((v,w))
            vedges[v].append((u,w))
        inf=float('inf')
        dist=defaultdict(lambda:inf)
        dist[(0,0)]=0
        pq=[(0,0,0)]
        while pq:
            cost,node,used=heapq.heappop(pq)
            if cost>dist[(node,used)]:
                continue
            for nxt,w in uedges[node]:
                newcost=cost+w
                if newcost<dist[(nxt,used)]:
                    dist[(nxt,used)]=newcost
                    heapq.heappush(pq,(newcost,nxt,used))
            if not (used&(1<<node)):
                newused=used|(1<<node)
                for prev,w in vedges[node]:
                    newcost=cost+2*w
                    if newcost<dist[(prev,newused)]:
                        dist[(prev,newused)]=newcost
                        heapq.heappush(pq,(newcost,prev,newused))
        ans=float('inf')
        for m in range(1<<n):
             if(n-1,m) in dist:
                ans=min(ans,dist[(n-1,m)])
        return -1 if ans==inf else ans




