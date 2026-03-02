class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        allowed=set(allowed)
        for i in words:
            counter=0
            for s in i:
                if s in allowed:
                    counter+=1
            if counter==len(i):
                count+=1
        return count