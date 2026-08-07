class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        temp=t
        for i in range(2,10):
            while temp%i==0:
                temp//=i
        if temp>1:
            return '-1'
        n=len(num)
        rem=[0]*(n+1)
        rem[0]=t
        pos=n-1
        new=list(num)
        for i in range(n):
            if new[i]=='0':
                pos=i
                break
            rem[i+1]=rem[i]//math.gcd(rem[i],int(new[i]))
        if rem[n]==1:
            return num
        for i in range(pos,-1,-1):
            while True:
                new[i]=chr(ord(new[i])+1)
                if new[i]>'9':
                    break
                now=rem[i]//math.gcd(rem[i],int(new[i]))
                k=9
                for j in range(n-1,i,-1):
                    while now%k!=0:
                        k-=1
                    now//=k
                    new[j]=str(k)
                if now==1:
                    return "".join(new)
        ans=[]
        original=t
        for i in range(9,1,-1):
            while original%i==0:
                ans.append(str(i))
                original//=i
        ansp=''.join(ans)
        pad=max(n+1-len(ansp),0)
        ansp+='1'*pad
        return ansp[::-1]