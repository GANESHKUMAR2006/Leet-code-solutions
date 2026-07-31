class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        res=""
        for i in range(n):
            l=i
            r=i
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            res=max(res,s[l+1:r],key=len)
            l=i
            r=i+1
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            res=max(res,s[l+1:r],key=len)
        return res