class Solution:
    def processStr(self, s: str, k: int) -> str:
        n=len(s)
        l=[0]*(n+1)
        for i,ch in enumerate(s):
            cur=l[i]
            if 'a'<=ch<='z':
                l[i+1]=cur+1
            elif ch=='*':
                l[i+1]=max(cur-1,0)
            elif ch=='#':
                l[i+1]=cur*2
            else:
                l[i+1]=cur
        final=l[n]
        if k>=final:
            return '.'
        for i in range(n-1,-1,-1):
            ch=s[i]
            prev=l[i]
            curr=l[i+1]
            if 'a'<=ch<='z':
                if k==curr-1:
                    return ch
            elif ch=='#':
                if prev>0 and k>=prev:
                    k-=prev
            elif ch=='%':
                if prev>0:
                    k=prev-1-k
            else:
                pass
        return '.'