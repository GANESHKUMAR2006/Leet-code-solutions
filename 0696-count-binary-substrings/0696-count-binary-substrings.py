class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cnt=1
        ans=0
        n=len(s)
        grp=[]
        for i in range(1,n):
            if s[i]==s[i-1]:
                cnt+=1
            else:
                grp.append(cnt)
                cnt=1
        grp.append(cnt)
        for i in range(1,len(grp)):
            ans+=min(grp[i],grp[i-1])
        return ans