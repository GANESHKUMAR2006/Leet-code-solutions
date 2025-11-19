class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt=0
        for i in words:
            if i[:len(pref)]==pref:
                cnt+=1
        return cnt