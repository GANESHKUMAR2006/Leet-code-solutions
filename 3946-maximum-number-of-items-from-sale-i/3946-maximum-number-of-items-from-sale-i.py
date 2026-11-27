class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n=len(items)
        val=[1]*n
        for i in range(n):
            fi=items[i][0]
            cnt=0
            for j in range(n):
                if i!=j and items[j][0]%fi==0:
                    cnt+=1
            val[i]=cnt+1
        pmin=min(price for _,price in items)
        arr=[-10**18]*(budget+1)
        arr[0]=0
        for i in range(n):
            cost=items[i][1]
            gain=val[i]
            for b in range(budget,cost-1,-1):
                arr[b]=max(arr[b],arr[b-cost]+gain)
        ans=budget//pmin
        for cost in range(budget+1):
            if arr[cost]>-10**18:
                ans=max(ans,arr[cost]+(budget-cost)//pmin)
        return ans