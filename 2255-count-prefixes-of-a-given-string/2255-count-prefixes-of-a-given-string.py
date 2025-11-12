class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        cnt=0
        for i in words:
            if s.startswith(i):
                cnt+=1
        return cnt