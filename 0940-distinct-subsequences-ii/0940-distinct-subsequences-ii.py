class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod=10**9+7
        dp=1
        last=[0]*26
        for ch in s:
            c=ord(ch)-ord('a')
            new=2*dp-last[c]
            new%=mod
            last[c]=dp
            dp=new
        return (dp-1)%mod
