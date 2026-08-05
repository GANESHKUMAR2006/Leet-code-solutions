class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(n)]
        for u,v in invocations:
            graph[u].append(v)
        sus=[False]*n
        q=deque([k])
        sus[k]=True
        while q:
            u=q.popleft()
            for v in graph[u]:
                if not sus[v]:
                    sus[v]=True
                    q.append(v)
        for u,v in invocations:
            if not sus[u] and sus[v]:
                return list(range(n))
        return [i for i in range(n) if not sus[i]]