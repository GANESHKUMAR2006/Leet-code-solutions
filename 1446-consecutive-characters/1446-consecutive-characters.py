class Solution:
    def maxPower(self, s: str) -> int:
        count=1
        mx=1
        n=len(s)
        for i in range(n):
            if i+1<n and s[i]==s[i+1]:
                count+=1
                mx=max(mx,count)
            else:
                count=1
        return mx