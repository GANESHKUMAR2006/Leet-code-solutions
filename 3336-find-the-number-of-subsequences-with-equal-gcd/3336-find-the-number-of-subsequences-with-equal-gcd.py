class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        mod=1000000007
        m=max(nums)
        dp=[[0]*(m+1) for _ in range(m+1)]
        dp[0][0]=1
        for num in nums:
            ndp=[[0]*(m+1) for _ in range(m+1)]
            for j in range(m+1):
                div=math.gcd(j,num)
                for k in range(m+1):
                    val=dp[j][k]
                    if val==0:
                        continue
                    div2=math.gcd(k,num)
                    ndp[j][k]=(ndp[j][k]+val)%mod
                    ndp[div][k]=(ndp[div][k]+val)%mod
                    ndp[j][div2]=(ndp[j][div2]+val)%mod
            dp=ndp
        ans=0
        for o in range(1,m+1):
            ans=(ans+dp[o][o])%mod
        return ans



