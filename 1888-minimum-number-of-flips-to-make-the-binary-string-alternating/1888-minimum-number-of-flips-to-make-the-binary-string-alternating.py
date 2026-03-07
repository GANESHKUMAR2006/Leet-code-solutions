class Solution:
    def minFlips(self, s: str) -> int:
        n=len(s)
        s=s+s
        alt=""
        alt2=""
        for i in range(len(s)):
            if i%2==0:
                alt+='0'
                alt2+='1'
            else:
                alt+='1'
                alt2+='0'
        res=float('inf')
        diff=diff2=0
        l=0
        for r in range(len(s)):
            if s[r]!=alt[r]:
                diff+=1
            if s[r]!=alt2[r]:
                diff2+=1
            if r-l+1>n:
                if s[l]!=alt[l]:
                    diff-=1
                if s[l]!=alt2[l]:
                    diff2-=1
                l+=1
            if r-l+1==n:
                res=min(res,diff,diff2)
        return res