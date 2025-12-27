class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        count=Counter(words)
        container=[]
        for i,j in count.items():
            container.append((-j,i))
        container.sort()
        return [j for i,j in container[:k]]