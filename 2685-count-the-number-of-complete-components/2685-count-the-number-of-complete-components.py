class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g=[[] for _ in range(n)]
        com=defaultdict(int)
        for v in range(n):
            g[v]=[v]
        for v1,v2 in edges:
            g[v1].append(v2)
            g[v2].append(v1)
        for v in range(n):
            nei=tuple(sorted(g[v]))
            com[nei]+=1
        return sum(1 for nei,freq in com.items() if len(nei)==freq)