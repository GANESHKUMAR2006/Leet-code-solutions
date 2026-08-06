class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def product(x):
            p=1
            while x:
                p*=x%10
                x//=10
            return p
        while True:
            if product(n)%t==0:
                return n
            n+=1