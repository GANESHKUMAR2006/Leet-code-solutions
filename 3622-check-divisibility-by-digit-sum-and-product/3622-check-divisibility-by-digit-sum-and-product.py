class Solution:
    def checkDivisibility(self, n: int) -> bool:
        n=str(n)
        add=0
        product=1
        for i in n:
            add+=int(i)
            product*=int(i)
        n=int(n)
        return n%(add+product)==0