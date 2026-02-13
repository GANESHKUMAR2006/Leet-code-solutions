class Solution:
    def longestBalanced(self, s: str) -> int:
        n=len(s)
        ans,Len=1,1
        for c0,c1 in pairwise(s):
            if c0==c1: Len+=1
            else:
                ans=max(ans,Len)
                Len=1
        ans=max(ans,Len)
        ab,bc,ca,abc={},{},{},{}
        abc[(0,0)]=ab[(0,0)]=bc[(0,0)]=ca[(0,0)]=-1
        cnt=[0,0,0]
        for i,ch in enumerate(s):
            cnt[ord(ch)-97]+=1
            a,b,c=cnt
            key=(b-a,c-a)
            if key in abc: ans=max(ans,i-abc[key])
            else: abc[key]=i
            key=(a-b,c)
            if key in ab: ans=max(ans,i-ab[key])
            else:ab[key]=i
            key=(b-c,a)
            if key in bc: ans=max(ans,i-bc[key])
            else: bc[key]=i
            key=(c-a,b)
            if key in ca: ans=max(ans,i-ca[key])
            else: ca[key]=i
        return ans