class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        cnt=s.count('1')
        n=len(s)
        i=0
        best=0
        prev=float('-inf')
        while i<n:
            start=i
            while i<n and s[i]==s[start]:
                i+=1
            if s[start]=='0':
                cur=i-start
                best=max(best,prev+cur)
                prev=cur
        return cnt+best            