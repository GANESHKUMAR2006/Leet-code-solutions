class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        parent=list(range(len(source)))
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(a,b):
            pa,pb=find(a),find(b)
            if pa!=pb:
                parent[pb]=pa
        for a,b in allowedSwaps:
            union(a,b)
        grp=defaultdict(list)
        for i in range(len(source)):
            grp[find(i)].append(i)
        answer=0
        for indices in grp.values():
            freq=Counter(source[i] for i in indices)
            for i in indices:
                if freq[target[i]]>0:
                    freq[target[i]]-=1
                else:
                    answer+=1
        return answer