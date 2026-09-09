class Solution:
    def countCommas(self, n: int) -> int:
        ans=0
        power=1000
        comas=1
        while power<=n:
            ans+=n-power+1
            power*=1000
            comas+=1
        return ans