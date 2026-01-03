class Solution:
    def numOfWays(self, n: int) -> int:
        mod=(10**9)+7
        a=6
        b=6
        for _ in range(1,n):
            a,b=(a*3+b*2)%mod,(a*2+b*2)%mod
        return (a+b)%mod