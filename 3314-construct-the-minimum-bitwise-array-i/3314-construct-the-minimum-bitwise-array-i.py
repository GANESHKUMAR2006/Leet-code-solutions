class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for n in nums:
            if not n%2:
                ans.append(-1)
            else:
                val=format(n,'b')
                val=val[::-1]
                count=0
                for i in val:
                    if i=='1':
                        count+=1
                    else:
                        break
                k=count
                x=n-(2**(k-1))
                if (x)|(x+1)==n:
                    ans.append(min(x,x+1))
        return ans

