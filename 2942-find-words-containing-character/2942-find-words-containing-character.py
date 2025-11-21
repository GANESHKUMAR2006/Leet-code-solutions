class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res=[]
        n=len(words)
        for i in range(n):
            if words[i].count(x):
                res.append(i)
        return res