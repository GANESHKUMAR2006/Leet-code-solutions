class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        res=[0]*(26)
        upper=lower=set()
        for c in word:
            if ord(c)>96 and c not in upper:
                res[97-ord(c)]+=1
                upper.add(c)
            if ord(c)<91 and c not in lower:
                res[65-ord(c)]+=1
                lower.add(c)
        count=0
        for num in res:
            if num==2:
                count+=1
        return count