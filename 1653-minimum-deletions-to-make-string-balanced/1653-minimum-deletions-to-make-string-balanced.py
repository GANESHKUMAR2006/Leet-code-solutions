class Solution:
    def minimumDeletions(self, s: str) -> int:
        bcount=0
        res=0
        n=len(s)
        for i in range(n):
            if s[i]=='b':
                bcount+=1
            elif bcount:
                bcount-=1
                res+=1
        return res