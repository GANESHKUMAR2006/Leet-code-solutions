class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        mod=10**9+7
        n=len(s)
        pref_sum=[0]*(n+1)
        pref_cnt=[0]*(n+1)
        pref_num=[0]*(n+1)
        for i in range(n):
            digit=int(s[i])
            pref_sum[i+1]=pref_sum[i]+digit
            pref_cnt[i+1]=pref_cnt[i]+(digit!=0)
            if digit!=0:
                pref_num[i+1]=(pref_num[i]*10+digit)%mod
            else:
                pref_num[i+1]=pref_num[i]
        res=[]
        for l,r in queries:
            digit_sum=pref_sum[r+1]-pref_sum[l]
            cnt=pref_cnt[r+1]-pref_cnt[l]
            if cnt==0:
                res.append(0)
                continue
            num_right=pref_num[r+1]
            num_left=pref_num[l]
            total=(num_right-(num_left*pow(10,cnt,mod))%mod+mod)%mod
            ans=(total*digit_sum)%mod
            res.append(ans)
        return res