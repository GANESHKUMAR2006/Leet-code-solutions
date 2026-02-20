class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        res=[]
        balance=0
        start=0
        for i,val in enumerate(s):
            if val=='1':
                balance+=1
            elif val=='0':
                balance-=1
            if balance==0:
                val=self.makeLargestSpecial(s[start+1:i])
                res.append('1'+val+'0')
                start=i+1
        res.sort(reverse=True)
        return ''.join(res)