class Solution:
    def sumAndMultiply(self, n: int) -> int:
        val=0
        sum=0
        while n>0:
            if n%10!=0:
                sum+=n%10
                val=val*10+(n%10)
                n//=10
            else:
                n//=10
        val=str(val)
        val=val[::-1]
        return int(val)*sum