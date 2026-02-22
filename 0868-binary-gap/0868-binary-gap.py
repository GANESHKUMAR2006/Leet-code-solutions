class Solution:
    def binaryGap(self, n: int) -> int:
        n=format(n,'b')
        ans=0
        left=0
        for i in range(1,len(n)):
            if n[i]=='1':
                ans=max(ans,i-left)
                left=i
        return ans