class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        filtered=[]
        for coin in coins:
            if not any(coin%prev==0 for prev in filtered):
                filtered.append(coin)
        coins=filtered
        n=len(coins)
        def lcm(a,b):
            return a//gcd(a,b)*b
        def count(x):
            ans=0
            for mask in range(1,1<<n):
                cur=1
                bits=0
                valid=True
                for i in range(n):
                    if mask & (1<<i):
                        cur=lcm(cur,coins[i])
                        bits+=1
                        if cur>x:
                            valid=False
                            break
                if not valid:
                    continue
                if bits%2==1:
                    ans+=x//cur
                else:
                    ans-=x//cur
            return ans
        left=1
        right=min(coins)*k
        while left<right:
            mid=(left+right)//2
            if count(mid)>=k:
                right=mid
            else:
                left=mid+1
        return left