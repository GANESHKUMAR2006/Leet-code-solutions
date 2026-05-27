class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        res=[0]*26
        for c in word:
            idx=ord(c.lower())-ord('a')
            if c.islower():
                if res[idx]==0:
                    res[idx]=1
                elif res[idx]==2:
                    res[idx]=-1
            else:
                if res[idx]==1:
                    res[idx]=2
                elif res[idx]==0:
                    res[idx]=-1
        count=0
        for num in res:
            if num==2:
                count+=1
        return count