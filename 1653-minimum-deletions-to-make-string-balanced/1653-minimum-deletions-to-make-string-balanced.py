class Solution:
    def minimumDeletions(self, s: str) -> int:
        bcount=0
        res=0
        for i in s:
            if i=='b':
                bcount+=1
            elif bcount:
                bcount-=1
                res+=1
        return res