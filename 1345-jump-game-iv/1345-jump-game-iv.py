class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n=len(arr)
        if n==1:
            return 0
        mp=defaultdict(list)
        for i,num in enumerate(arr):
            mp[num].append(i)
        q=deque([(0,0)])
        v=set([0])
        while q:
            idx,steps=q.popleft()
            if idx==n-1:
                return steps
            neigh=mp[arr[idx]]+[idx-1,idx+1]
            for nxt in neigh:
                if 0<=nxt<n and nxt not in v:
                    v.add(nxt)
                    q.append((nxt,steps+1))
            mp[arr[idx]].clear()
                