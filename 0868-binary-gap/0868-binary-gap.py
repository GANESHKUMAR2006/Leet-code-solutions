class Solution:
    def binaryGap(self, n: int) -> int:
        n=format(n,'b')
        ans=0
        left=0
        for right in range(1,len(n)):
            if n[right]=='1':
                ans=max(ans,right-left)
                left=right
        return ans