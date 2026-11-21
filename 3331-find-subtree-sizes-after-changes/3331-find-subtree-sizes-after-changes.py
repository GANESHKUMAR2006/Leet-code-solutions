class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        nearest = [-1] * 26
        new_parent = parent[:]
        def dfs(node):
            c = ord(s[node]) - ord('a')
            prev = nearest[c]
            if prev != -1:
                new_parent[node] = prev
            nearest[c] = node
            for child in children[node]:
                dfs(child)
            nearest[c] = prev
        dfs(0)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[new_parent[i]].append(i)
        answer = [1] * n
        def calculate(node):
            for child in children[node]:
                calculate(child)
                answer[node] += answer[child]
        calculate(0)
        return answer